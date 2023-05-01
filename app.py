import instaloader
from instaloader.exceptions import BadResponseException
from instagrapi import Client
from flask import Flask, jsonify

app = Flask(__name__)
cl = Client()

def obter_InstaloaderInfo(url):
    L = instaloader.Instaloader()
    shortcode = url.split("/")[-2]
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        if isinstance(post, tuple):
            return [], "", False, ''
        urls = []
        if post.typename == 'GraphSidecar':
            for index, node in enumerate(post.get_sidecar_nodes()):
                urls.append(node.video_url if node.is_video else node.display_url)
        elif post.is_video:
            urls.append(post.video_url)
        else:
            urls.append(post.url)
        
        return urls, post.owner_username, True, 'instaloader'
    except BadResponseException:
        return [], "", False, ''

def obter_InstagrapiInfo(url):
    try:
        media_id = cl.media_pk_from_url(url)
        media_info = cl.media_info(media_id).dict()

        urls = []
        if 'resources' in media_info and media_info['resources']:
            urls = [resource['thumbnail_url'] for resource in media_info['resources'] if resource['media_type'] == 1 and 'profile_pic_url' not in resource['thumbnail_url']]
        elif media_info['media_type'] == 1 and 'thumbnail_url' in media_info:
            urls.append(media_info['thumbnail_url'])
        elif media_info['media_type'] == 2 and 'video_url' in media_info:
            urls.append(media_info['video_url'])

        return urls, media_info['user']['username'], True, 'instagrapi'
    except Exception as e:
        return [], "", False, ''

@app.route('/api/<path:url>', methods=['GET'])
def obter_Media(url):
    urls, username, success, client = obter_InstaloaderInfo(f'https://www.instagram.com/{url}')
    
    if not success:
        urls, username, success, client = obter_InstagrapiInfo(f'https://www.instagram.com/{url}')
    
    if success:
        return jsonify({'urls': urls, 'username': username, 'success': success, 'client': client})
    else:
        return jsonify({'error': 'Não foi possível obter informações do post.', 'success': success, 'client': client})

if __name__ == '__main__':
    app.run(debug=True)