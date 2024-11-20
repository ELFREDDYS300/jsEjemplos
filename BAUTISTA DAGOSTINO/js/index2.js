function evento(event) {
    let boxes = document.querySelectorAll('.box');
    
    boxes.forEach(box => {
        box.style.transition = 'width 0.5s ease, transform 0.3s ease';  
        box.style.width = '300px'; 
        box.style.transform = 'scale(1)'; 
    });

    let currentBox = event.currentTarget;
    
   
    currentBox.style.width = '500px';
    currentBox.style.transform = 'scale(1.1)';
}
