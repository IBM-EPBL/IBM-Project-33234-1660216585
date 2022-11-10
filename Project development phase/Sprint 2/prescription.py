<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Meta Info -->
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>personal assistance - Prescriptions</title>
    <!-- Styles -->
    <link rel="stylesheet" href="static/styles.css" />
    <!-- For plain html -->
    <link rel="stylesheet" href="../../static/styles.css" />
  </head>
  <body>
    <div class="flex flex-no-wrap">
      <!-- Sidebar starts -->
      <div class="fixed">
        <div class="w-64 h-screen sm:relative bg-primary-blue-light shadow flex-col justify-between hidden sm:flex">
          <div class="px-8 h-full">
            <div class="h-16 w-full flex items-center">
              <img src="../../static/img/logo.png" />
            </div>
            <ul class="mt-12">
              <li class="flex w-full justify-between text-gray-400 hover:text-gray-300 cursor-pointer items-center mb-6">
                <a href="/dashboard" class="flex items-center focus:outline-none focus:ring-2 focus:ring-white">
                <object type="image/svg+xml" data="../../static/svg/dashboard.svg"></object>
                <span class="text-sm ml-2">Dashboard</span>
                </a>
              </li>
              <li class="flex w-full justify-between text-white cursor-pointer items-center mb-6">
                <a href="/schedule" class="flex items-center focus:outline-none focus:ring-2 focus:ring-white">
                <object type="image/svg+xml" data="../../static/svg/plugin.svg"></object>
                <span class="text-sm ml-2">Schedule</span>
                </a>
                <div class="py-1 px-3 bg-white rounded text-primary-blue-light flex items-center justify-center text-xs">{{ upcoming_count }}</div>
              </li>
              <li class="flex w-full justify-between text-gray-400 hover:text-gray-300 cursor-pointer items-center mb-6">
                <a href="/medicines" class="flex items-center focus:outline-none focus:ring-2 focus:ring-white">
                <object type="image/svg+xml" data="../../static/svg/compass-inactive.svg"></object>
                <span class="text-sm ml-2">Medicines</span>
                </a>
              </li>
              <li class="flex w-full justify-between text-gray-400 hover:text-gray-300 cursor-pointer items-center mb-6">
                <a href="/prescription" class="flex items-center focus:outline-none focus:ring-2 focus:ring-white">
                <object type="image/svg+xml" data="../../static/svg/plugin-inactive.svg"></object>
                <span class="text-sm ml-2">Prescription</span>
                </a>
              </li>
              <li class="flex w-full justify-between text-gray-400 hover:text-gray-300 cursor-pointer items-center">
                <a href="/login" class="flex items-center focus:outline-none focus:ring-2 focus:ring-white">
                <object type="image/svg+xml" data="../../static/svg/settings-inactive.svg"></object>
                <span class="text-sm ml-2">Logout</span>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="w-64 z-40 fixed h-screen bg-primary-blue-light shadow flex-col justify-between sm:hidden transition duration-150 ease-in-out" id="mobile-nav">
        <button aria-label="toggle sidebar" id="openSideBar" class="h-10 w-10 bg-primary-blue-light absolute right-0 mt-16 -mr-10 flex items-center shadow rounded-tr rounded-br justify-center cursor-pointer focus:outline-none focus:ring-2 focus:ring-offset-2 rounded focus:ring-gray-800" onclick="sidebarHandler(true)">
          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-adjustments" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="#FFFFFF" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <path stroke="none" d="M0 0h24v24H0z" />
            <circle cx="6" cy="10" r="2" />
            <line x1="6" y1="4" x2="6" y2="8" />
            <line x1="6" y1="12" x2="6" y2="20" />
            <circle cx="12" cy="16" r="2" />
            <line x1="12" y1="4" x2="12" y2="14" />
            <line x1="12" y1="18" x2="12" y2="20" />
            <circle cx="18" cy="7" r="2" />
            <line x1="18" y1="4" x2="18" y2="5" />
            <line x1="18" y1="9" x2="18" y2="20" />
          </svg>
        </button>
        <button aria-label="Close sidebar" id="closeSideBar" class="hidden h-10 w-10 bg-gray-800 absolute right-0 mt-16 -mr-10 flex items-center shadow rounded-tr rounded-br justify-center cursor-pointer text-white" onclick="sidebarHandler(false)">
          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-x" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <path stroke="none" d="M0 0h24v24H0z" />
            <line x1="18" y1="6" x2="6" y2="18" />
            <line x1="6" y1="6" x2="18" y2="18" />
          </svg>
        </button>
        <div class="flex flex-col px-8 h-full">
          <div class="h-14 w-full flex items-center">
            <img class="mt-3" src="../../static/img/logo.png" />
          </div>
          <ul class="mt-12">
            <li class="flex w-full justify-between text-gray-400 hover:text-gray-300 cursor-pointer items-center mb-6">
              <a href="/dashboard" class="flex items-center focus:outline-none focus:ring-2 focus:ring-white">
              <object ype="image/svg+xml" data="../../static/svg/dashboard.svg"></object>
              <span class="text-sm ml-2">Dashboard</span>
              </a>
            </li>
            <li class="flex w-full justify-between text-white cursor-pointer items-center mb-6">
              <a href="/schedule" class="flex items-center focus:outline-none focus:ring-2 focus:ring-white">
              <object type="image/svg+xml" data="../../static/svg/plugin.svg"></object>
              <span class="text-sm ml-2">Schedule</span>
              </a>
              <div class="py-1 px-3 bg-white rounded text-primary-blue-light flex items-center justify-center text-xs">{{ upcoming_count }}</div>
            </li>
            <li class="flex w-full justify-between text-gray-400 hover:text-gray-300 cursor-pointer items-center mb-6">
              <a href="/medicines" class="flex items-center focus:outline-none focus:ring-2 focus:ring-white">
              <object type="image/svg+xml" data="../../static/svg/compass-inactive.svg"></object>
              <span class="text-sm ml-2">Medicines</span>
              </a>
            </li>
            <li class="flex w-full justify-between text-gray-400 hover:text-gray-300 cursor-pointer items-center mb-6">
              <a href="/prescription" class="flex items-center focus:outline-none focus:ring-2 focus:ring-white">
              <object type="image/svg+xml" data="../../static/svg/plugin-inactive.svg"></object>
              <span class="text-sm ml-2">Prescription</span>
              </a>
            </li>
            <li class="flex w-full justify-between text-gray-400 hover:text-gray-300 cursor-pointer items-center">
              <a href="/login" class="flex items-center focus:outline-none focus:ring-2 focus:ring-white">
              <object type="image/svg+xml" data="../../static/svg/settings-inactive.svg"></object>
              <span class="text-sm ml-2">Logout</span>
              </a>
            </li>
          </ul>
          <div class="h-full"></div>
          <div class="px-8 border-t border-gray-400">
            <ul class="w-full flex items-center justify-between bg-primary-blue-light">
              <li class="cursor-pointer text-white pt-5 pb-3">
                <button aria-label="show notifications" class="focus:outline-none focus:ring-2 rounded focus:ring-gray-300">
                <i class="fas fa-bell"></i>
                </button>
              </li>
              <li class="cursor-pointer text-white pt-5 pb-3">
                <button aria-label="open chats" class="focus:outline-none focus:ring-2 rounded focus:ring-gray-300">
                <i class="fas fa-comments"></i>
                </button>
              </li>
              <li class="cursor-pointer text-white pt-5 pb-3">
                <button aria-label="open settings" class="focus:outline-none focus:ring-2 rounded focus:ring-gray-300">
                <i class="fas fa-cog"></i>
                </button>
              </li>
              <li class="cursor-pointer text-white pt-5 pb-3">
                <button aria-label="open logs" class="focus:outline-none cursor-pointer focus:ring-2 rounded focus:ring-gray-300">
                <i class="fas fa-plus"></i>
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <!-- Sidebar ends -->
      <!-- Container Start -->
      <div class="sm:ml-64  w-full">
        <div class="container mx-auto h-64 md:w-4/5 w-full px-4 flex flex-col flex-no-wrap">
          <div class="flex flex-col my-9">
            <p class="text-3xl font-semibold my-7 dark:text-white">Prescriptions</p>
            <p class="text-sm text-gray-700 dark:text-gray-200">
              Click <span class="bg-gray-200 text-primary-blue-light">+</span> at the bootom right to store your prescriptions with us. Powered by CodeTech Drive.

            </p>
          </div>
          <!-- Columns  -->
          <div class="flex flex-wrap w-full flex-col lg:flex-row">
            <!-- Column 1 (Next Up)-->
            <div class="my-2 mx-2 flex-1 flex flex-col">
              <!-- Column Header  -->
              <div class="flex rounded-md bg-gray-200 p-2">
                <p class="text-gray-900 font-semibold">Your prescriptions</p>
                <div class="flex-grow"></div>
                <!-- Spacer -->
                <div class="py-1 px-3 bg-gray-800 rounded text-white flex items-center justify-center text-xs">{{ total }}</div>
              </div>
              <!-- Column Cards  -->
              <div class="flex-col flex md:flex-row lg:flex-col">
              {{ prescription_card_html|safe }}
              </div>
            </div>
            <!-- Column 2 (Completed)-->
          </div>
        </div>
      </div>
      <!-- Container End -->
      <a href="/prescription/add">
        <button
          class="fixed bottom-3 right-3 p-0 w-16 h-16 bg-primary-blue-light rounded-full hover:bg-blue-700 active:shadow-lg mouse shadow transition ease-in duration-200 focus:outline-none">
          <svg viewBox="0 0 20 20" enable-background="new 0 0 20 20" class="w-6 h-6 inline-block">
            <path fill="#FFFFFF" d="M16,10c0,0.553-0.048,1-0.601,1H11v4.399C11,15.951,10.553,16,10,16c-0.553,0-1-0.049-1-0.601V11H4.601
              C4.049,11,4,10.553,4,10c0-0.553,0.049-1,0.601-1H9V4.601C9,4.048,9.447,4,10,4c0.553,0,1,0.048,1,0.601V9h4.399
              C15.952,9,16,9.447,16,10z" />
      </a>
      </svg>
      </button>
    </div>
    <script defer src="../../static/@fortawesome/fontawesome-free/js/brands.js"></script>
    <script defer src="../../static/@fortawesome/fontawesome-free/js/solid.js"></script>
    <script defer src="../../static/@fortawesome/fontawesome-free/js/fontawesome.js"></script>
    <script>
      var sideBar = document.getElementById("mobile-nav");
      var toggler = document.getElementById("mobile-toggler");
      sideBar.style.transform = "translateX(-260px)";
      let moved = true;

      function sidebarHandler() {
        if (moved) {
          sideBar.style.transform = "translateX(0px)";
          moved = false;
        } else {
          sideBar.style.transform = "translateX(-260px)";
          moved = true;
        }
      }
    </script>
  </body>
</html>