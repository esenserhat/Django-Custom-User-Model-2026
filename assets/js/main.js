// Profile Dropdown Toggle
const profil_buton = document.getElementById('profil_buton');
const profil_menu = document.getElementById('profil_menu');

profil_buton?.addEventListener('click', (e) => {
    e.stopPropagation();
    profil_menu.classList.toggle('hidden');
});

// Close profile menu when clicking outside
document.addEventListener('click', (e) => {
    if (!profil_buton?.contains(e.target) && !profil_menu?.contains(e.target)) {
        profil_menu?.classList.add('hidden');
    }
});

// App Selector Dropdown Toggle
const app_selector_buton = document.getElementById('app_selector_buton');
const app_selector_menu = document.getElementById('app_selector_menu');

app_selector_buton?.addEventListener('click', (e) => {
    e.stopPropagation();
    app_selector_menu.classList.toggle('hidden');
});

// App Selector Dropdown Toggle (Mobil)
const app_selector_buton_mobil = document.getElementById('app_selector_buton_mobil');
const app_selector_menu_mobil = document.getElementById('app_selector_menu_mobil');

app_selector_buton_mobil?.addEventListener('click', (e) => {
    e.stopPropagation();
    app_selector_menu_mobil.classList.toggle('hidden');
});

// Close app selector menu when clicking outside
document.addEventListener('click', (e) => {
    if (!app_selector_buton?.contains(e.target) && !app_selector_menu?.contains(e.target)) {
        app_selector_menu?.classList.add('hidden');
    }
    if (!app_selector_buton_mobil?.contains(e.target) && !app_selector_menu_mobil?.contains(e.target)) {
        app_selector_menu_mobil?.classList.add('hidden');
    }
});

// Sidebar Toggle
const mobil_sidebar_buton = document.getElementById('mobil_sidebar_buton');
const sidebar = document.getElementById('sidebar');
const eoSidebar = document.getElementById('eoSidebar');
const closeSidebar = document.getElementById('closeSidebar');

function openSidebar() {
    sidebar.classList.remove('-translate-x-full');
    eoSidebar.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeSidebarFunc() {
    sidebar.classList.add('-translate-x-full');
    eoSidebar.classList.add('hidden');
    document.body.style.overflow = '';
}

mobil_sidebar_buton?.addEventListener('click', openSidebar);
closeSidebar?.addEventListener('click', closeSidebarFunc);
eoSidebar?.addEventListener('click', closeSidebarFunc);

// Close sidebar on window resize to desktop
window.addEventListener('resize', () => {
    if (window.innerWidth >= 1024) {
        closeSidebarFunc();
    }
});

// Button Loading
function setButtonLoading(button, duration = 3) {
    const btn = typeof button === 'string' ? document.getElementById(button) : button;
    
    if (!btn) return;
    if (btn.dataset.loading === 'true') return;
    
    const originalContent = btn.innerHTML;
    const originalClasses = btn.className;
    
    btn.dataset.loading = 'true';
    btn.dataset.originalContent = originalContent;
    btn.dataset.originalClasses = originalClasses;
    
    btn.style.pointerEvents = 'none';
    btn.style.position = 'relative';
    
    btn.innerHTML = `
        <span class="opacity-50 flex items-center gap-2">
            <span class="relative flex h-3 w-3">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-current opacity-75"></span>
                <span class="relative inline-flex rounded-full h-3 w-3 bg-current"></span>
            </span>
            <span>Bekleyiniz...</span>
        </span>
    `;
    
    setTimeout(() => {
        btn.innerHTML = btn.dataset.originalContent;
        btn.className = btn.dataset.originalClasses;
        btn.style.pointerEvents = '';
        btn.style.position = '';
        
        delete btn.dataset.loading;
        delete btn.dataset.originalContent;
        delete btn.dataset.originalClasses;
    }, duration * 1000);
}

document.addEventListener('click', (e) => {
    const target = e.target.closest('[eo-loading]');
    if (target) {
        const duration = parseInt(target.getAttribute('eo-loading-duration')) || 3;
        setButtonLoading(target, duration);
    }
});

// eo-tab: Basit tab sistemi (eo-tab-href ile)
document.addEventListener('DOMContentLoaded', function () {
    const tabContainers = document.querySelectorAll('.card .-mb-px');
    tabContainers.forEach(function (tabContainer) {
        const tabs = tabContainer.querySelectorAll('.eo-tab');
        const card = tabContainer.closest('.card');
        if (!card) return;
        const tabContents = card.querySelectorAll('[eo-tab-content]');

        tabs.forEach(function (tab) {
            tab.style.cursor = 'pointer';
            tab.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                // Aktif tabı değiştir
                tabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                // İçerikleri göster/gizle
                const tabName = tab.getAttribute('eo-tab-href');
                tabContents.forEach(content => {
                    if (content.getAttribute('eo-tab-content') === tabName) {
                        content.style.display = '';
                    } else {
                        content.style.display = 'none';
                    }
                });
            });
        });
        // Sayfa yüklenince sadece aktif tab içeriği göster
        let anyActive = false;
        tabs.forEach((tab, i) => {
            const tabName = tab.getAttribute('eo-tab-href');
            if (tab.classList.contains('active')) {
                anyActive = true;
                tabContents.forEach(content => {
                    content.style.display = (content.getAttribute('eo-tab-content') === tabName) ? '' : 'none';
                });
            }
        });
        // Eğer hiç aktif tab yoksa ilkini aktif yap
        if (!anyActive && tabs.length > 0) {
            tabs[0].classList.add('active');
            const tabName = tabs[0].getAttribute('eo-tab-href');
            tabContents.forEach(content => {
                content.style.display = (content.getAttribute('eo-tab-content') === tabName) ? '' : 'none';
            });
        }
    });
});


