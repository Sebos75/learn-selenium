console.log('start');

setTimeout(() => {
    document.getElementById('my-title').classList.add('extra1');
}, 1000);
document.getElementById('add-btn').addEventListener('click', addClassHandler);

function addClassHandler() {
    document.getElementById('my-title').classList.add('extra1');
}
