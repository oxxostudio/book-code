let uri = '你的網址';
fetch(uri, {method:'GET'})
.then(res => {
    return res.text()
}).then(result => {
    console.log(result);
});
