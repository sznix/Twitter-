document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.js-menu-icon').forEach(function (icon) {
    icon.addEventListener('click', function () {
      var menu = this.nextElementSibling;
      menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
    });
  });
});
