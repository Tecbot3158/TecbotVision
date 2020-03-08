Download the latest releases from the chameleon-vision github repository.
[Download releases here](https://github.com/Chameleon-Vision/chameleon-vision/releases)
<code>
curl -s https://api.github.com/repos/Chameleon-Vision/chameleon-vision/releases/latest | jq -r ".assets[] | select(.name | contains(\"search param for specific download url\")) | .browser_download_url" | wget -i -
</code>
