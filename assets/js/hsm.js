document.addEventListener("DOMContentLoaded", function() {
	addBackToTop(
        {"zIndex":100}
   );
   
   renderMathInElement(document.body, {
     // ...options...
     delimiters:
     [
       {left: "$$", right: "$$", display: true},
       {left: "$", right: "$", display: false},
       {left: "\\(", right: "\\)", display: false},
       {left: "\\[", right: "\\]", display: true}
    ]
    });
    
    createToggler('#navToggler', '#docsNav', 'docsSliderActive');
    createToggler('#tocToggler', 'body', 'tocActive');

    var headings = document.querySelector('.toc-headings');
    headings && headings.addEventListener('click', function(event) {
      var el = event.target;
      while(el !== headings){
        if (el.tagName === 'A') {
          document.body.classList.remove('tocActive');
          break;
        } else{
          el = el.parentNode;
          }
       }
      }, false);

     function createToggler(togglerSelector, targetSelector, className) {
       var toggler = document.querySelector(togglerSelector);
       var target = document.querySelector(targetSelector);

       if (!toggler) {
         return;
       }

       toggler.onclick = function(event) {
         event.preventDefault();

         target.classList.toggle(className);
        };
      }
});

var coll = document.getElementsByClassName('collapsible');
      var checkActiveCategory = true;
      for (var i = 0; i < coll.length; i++) {
        var links = coll[i].nextElementSibling.getElementsByTagName('*');
        if (checkActiveCategory){
          for (var j = 0; j < links.length; j++) {
            if (links[j].classList.contains('navListItemActive')){
              coll[i].nextElementSibling.classList.toggle('hide');
              coll[i].childNodes[1].classList.toggle('rotate');
              checkActiveCategory = false;
              break;
            }
          }
        }

        coll[i].addEventListener('click', function() {
          var arrow = this.childNodes[1];
          arrow.classList.toggle('rotate');
          var content = this.nextElementSibling;
          content.classList.toggle('hide');
        });
      }