document.addEventListener('DOMContentLoaded', function () {
  // Toggle menu on icon click
  document.querySelectorAll('.js-menu-icon').forEach(function (icon) {
    icon.addEventListener('click', function (e) {
      e.stopPropagation();
      var menu = this.nextElementSibling;
      document.querySelectorAll('.menu').forEach(function (m) {
        if (m !== menu) m.style.display = 'none';
      });
      menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
    });
  });

  // Close menus when clicking outside
  document.addEventListener('click', function () {
    document.querySelectorAll('.menu').forEach(function (menu) {
      menu.style.display = 'none';
    });
  });

  // Auto-resize textarea
  document.querySelectorAll('.post_form textarea').forEach(function (textarea) {
    textarea.addEventListener('input', function () {
      this.style.height = 'auto';
      this.style.height = this.scrollHeight + 'px';
    });
  });

  // Character counter
  document.querySelectorAll('.textarea-wrap textarea').forEach(function (textarea) {
    var counter = textarea.parentElement.querySelector('.char-count');
    if (!counter) return;
    var max = parseInt(textarea.getAttribute('maxlength'), 10) || 140;

    textarea.addEventListener('input', function () {
      var remaining = max - this.value.length;
      counter.textContent = remaining;
      counter.className = 'char-count';
      if (remaining <= 20) counter.classList.add('warn');
      if (remaining <= 10) counter.classList.add('danger');
    });
  });
});
