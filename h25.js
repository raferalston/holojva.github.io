while (true) {
    function runEvent(event){
           output.innerHTML = '<h3>MouseX ' + event.offsetX + ' </h3>' + '<h3>MouseY ' + event.offsetY + '</h3>';
           let iks = event.offsetX * 10.0392156863;
           let igrek = event.offsetY * 6.27450980392;
           box.style.backgroundColor = 'rgb(' + iks  + ' , ' + igrek + ', 40)' 
      }
}