function goAway() {
    document.getElementById('biscuits').remove();
    const date = new Date();
    date.setTime(date.getTime() + (28*24*60*60*1000));
    document.cookie = "goaway=True; expires=" + date.toUTCString() + "; path=/";
}
function goBack() {
    document.cookie = 'goaway=True; expires=Thu, 02 Sep 1945 00:00:00 UTC; path=/;';
}

function redirect() {
    window.location.href='https://www.reddit.com/r/productivity/comments/qe0qhr/why_do_we_procrastinate_when_its_plainly_in_our/';
}

function declined() {
    var audio = new Audio('britannia.mp3');
    audio.play();
    window.setTimeout(redirect, 3800);
}
