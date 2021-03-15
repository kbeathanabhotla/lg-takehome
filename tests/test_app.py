
def test_index(app, client):
    img_bytes = open('tests/dog.jpg', mode='r').read()
    print(img_bytes)
    res = client.post('/', data={'image_bytes': img_bytes})
    assert res.status_code == 200
