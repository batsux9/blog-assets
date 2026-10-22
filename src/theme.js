/* Theme-only interactions. Tumblr owns search, posts, likes, reblogs and pages. */
(() => {
  const root = document.documentElement;
  const themeButton = document.getElementById('themeButton');
  const menuButton = document.getElementById('menuButton');
  const sidebar = document.getElementById('sidebar');
  // Keep the active sidebar item in sync with the actual route, including
  // Tumblr Custom Pages and links configured through the theme options.
  const cleanPath = (path) => path.replace(/\/+$/, '') || '/';
  const currentPath = cleanPath(window.location.pathname);
  document.querySelectorAll('.side-nav .nav-item').forEach((link) => {
    const destination = new URL(link.href, window.location.href);
    const targetPath = cleanPath(destination.pathname);
    const isHome = targetPath === '/' &&
      (currentPath === '/' || /^\/page\/\d+$/.test(currentPath));
    const isCurrent = destination.origin === window.location.origin &&
      (isHome || (targetPath !== '/' && targetPath === currentPath));

    link.classList.toggle('active', isCurrent);
    if (isCurrent) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  });

  const chosen = window.localStorage.getItem('batsu-theme');
  if (chosen === 'light' || chosen === 'dark') root.dataset.theme = chosen;
  themeButton?.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    window.localStorage.setItem('batsu-theme', next);
  });
  menuButton?.addEventListener('click', () => {
    const open = sidebar?.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', String(Boolean(open)));
    menuButton.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      const openMenu = document.querySelector('.post-options[open]');
      if (openMenu) {
        openMenu.open = false;
        openMenu.querySelector('summary')?.focus();
      }
    }
    if (event.key === 'Escape' && sidebar?.classList.contains('open')) {
      sidebar.classList.remove('open');
      menuButton?.setAttribute('aria-expanded', 'false');
    }
  });

  const closeOtherPostMenus = (except) => {
    document.querySelectorAll('.post-options[open]').forEach((menu) => {
      if (menu !== except) menu.open = false;
    });
  };

  document.addEventListener('toggle', (event) => {
    const menu = event.target;
    if (!menu.matches?.('.post-options') || !menu.open) return;
    closeOtherPostMenus(menu);
    const copy = menu.querySelector('.post-options-copy');
    if (copy) copy.textContent = 'Copy link';
  }, true);

  document.addEventListener('click', async (event) => {
    const copy = event.target.closest('.post-options-copy');
    if (copy) {
      event.preventDefault();
      const url = copy.dataset.permalink;
      if (!url) return;
      try {
        if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(url);
        copy.textContent = 'Copied!';
      } catch {
        window.prompt('Copy post link:', url);
      }
      return;
    }
    closeOtherPostMenus(event.target.closest('.post-options'));
  });
  document.addEventListener('click', (event) => {
    if (!sidebar || !menuButton || !sidebar.classList.contains('open')) return;
    if (!sidebar.contains(event.target) && !menuButton.contains(event.target)) {
      sidebar.classList.remove('open');
      menuButton.setAttribute('aria-expanded', 'false');
    }
  });
})();
