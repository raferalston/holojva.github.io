let boxik = document.querySelector('#boxik')
    function runEvent(event){
           let a = window.innerWidth / 255
           let b = window.innerHeight / 255
           let iks = event.offsetX * a;
           let igrek = event.offsetY * b;
           boxik.style.backgroundColor = 'rgb(' + iks  + ' , ' + igrek + ', 40)' 
      }
boxik.addEventListener('mousemove', runEvent)
boxik.style.width = window.innerWidth; boxik.style.height = window.innerHeight;