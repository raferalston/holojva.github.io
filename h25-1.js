function letter(event) {
event.target.style.backgroundColor = 'purple'
}
let boxes = getElementsByTagName('div')
for (let i = 0; i < boxes.length; i++) {
    let element = boxes[i];
    element.addEventListener('click', letter)
}