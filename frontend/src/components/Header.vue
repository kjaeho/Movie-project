<template>
  <div v-if="isHeader" class="body">

    <!-- sidebar left align -->
    <nav class="navbar" style="overflow-y:hidden; overflow-x:hidden; z-index:1">
      <ul class="navbar-nav">
        <li class="logo">
          <a @click="goMain" class="nav-link" style="cursor:pointer">
            <span class="link-text logo-text" style="font-family: 'Black Han Sans', sans-serif;">팝콘 Angle</span>
            <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fad"
              data-icon="angle-double-right"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 448 512"
              class="svg-inline--fa fa-angle-double-right fa-w-14 fa-5x"
            >
              <g class="fa-group">
                <path
                  fill="currentColor"
                  d="M224 273L88.37 409a23.78 23.78 0 0 1-33.8 0L32 386.36a23.94 23.94 0 0 1 0-33.89l96.13-96.37L32 159.73a23.94 23.94 0 0 1 0-33.89l22.44-22.79a23.78 23.78 0 0 1 33.8 0L223.88 239a23.94 23.94 0 0 1 .1 34z"
                  class="fa-secondary"
                ></path>
                <path
                  fill="currentColor"
                  d="M415.89 273L280.34 409a23.77 23.77 0 0 1-33.79 0L224 386.26a23.94 23.94 0 0 1 0-33.89L320.11 256l-96-96.47a23.94 23.94 0 0 1 0-33.89l22.52-22.59a23.77 23.77 0 0 1 33.79 0L416 239a24 24 0 0 1-.11 34z"
                  class="fa-secondary"
                ></path>
              </g>
            </svg>
          </a>
        </li>
        <!-- Home button -->
        <li class="nav-item" style="cursor:pointer;" @click="goMain">
          <a class="nav-link">
            <svg
              aria-hidden="true"
              focusable="false"
              data-prefix="fas" 
              data-icon="home" 
              class="svg-inline--fa fa-home fa-w-18" 
              role="img" xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 576 512">
              <path 
                fill="currentColor" 
                d="M280.37 148.26L96 300.11V464a16 16 0 0 0 16 16l112.06-.29a16 16 0 0 0 15.92-16V368a16 16 0 0 1 16-16h64a16 16 0 0 1 16 16v95.64a16 16 0 0 0 16 16.05L464 480a16 16 0 0 0 16-16V300L295.67 148.26a12.19 12.19 0 0 0-15.3 0zM571.6 251.47L488 182.56V44.05a12 12 0 0 0-12-12h-56a12 12 0 0 0-12 12v72.61L318.47 43a48 48 0 0 0-61 0L4.34 251.47a12 12 0 0 0-1.6 16.9l25.5 31A12 12 0 0 0 45.15 301l235.22-193.74a12.19 12.19 0 0 1 15.3 0L530.9 301a12 12 0 0 0 16.9-1.6l25.5-31a12 12 0 0 0-1.7-16.93z"
                class="fa-secondary"
                >
              </path>
            </svg>
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Home</span>
          </a>
        </li>
        <!-- recommend button -->
        <li class="nav-item" style="cursor:pointer" @click="goRecommend">
          <a class="nav-link">
            <svg 
              height="512" 
              viewBox="0 0 64 64" 
              width="512" 
              xmlns="http://www.w3.org/2000/svg">
              <path class="fa-primary" fill="currentColor" d="m50 15h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m54 15h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m52 13h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m52 17h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m56 21h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m60 21h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m58 19h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m58 23h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m42 15h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m38 15h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m40 13h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m40 17h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m36 21h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m32 21h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m34 19h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m34 23h2v2h-2z"/>
              <path class="fa-primary" fill="currentColor" d="m63.339 31.691a1 1 0 0 0 -.951-.691h-11.029l-3.408-10.489a1 1 0 0 0 -1.9 0l-3.41 10.489h-11.029a1 1 0 0 0 -.588 1.809l8.922 6.483-3.408 10.489a1 1 0 0 0 1.539 1.119l8.923-6.483 8.923 6.483a1 1 0 0 0 1.539-1.118l-3.408-10.49 8.922-6.483a1 1 0 0 0 .363-1.118zm-11.049 6.409a1 1 0 0 0 -.363 1.118l2.681 8.253-7.02-5.1a1 1 0 0 0 -1.176 0l-7.02 5.1 2.681-8.253a1 1 0 0 0 -.363-1.118l-7.021-5.1h8.678a1 1 0 0 0 .951-.691l2.682-8.253 2.682 8.253a1 1 0 0 0 .951.691h8.678z"/>
              <path class="fa-secondary" fill="currentColor" d="m50 54h-17.649l-7.5-6h6.149a3 3 0 0 0 3-3v-.171a2.98 2.98 0 0 0 -.879-2.122l-1.513-1.507-6.94-6.067a2.988 2.988 0 0 0 -3.315-.424l-7.353 3.673v-.382a1 1 0 0 0 -1-1h-4a1 1 0 0 0 -1 1v.382l-4.553-2.282a1 1 0 0 0 -1.447.9v18a1 1 0 0 0 1.447.9l4.553-2.282v.382a1 1 0 0 0 1 1h4a.993.993 0 0 0 .93-.656l6.483 6.483a3.98 3.98 0 0 0 2.832 1.173h26.755a4 4 0 0 0 0-8zm-46-.618v-14.764l4 2v10.764zm8-.382h-2v-14h2zm38 7h-26.755a1.991 1.991 0 0 1 -1.418-.587l-7.827-7.827v-10.968l8.247-4.123a.993.993 0 0 1 1.105.141l6.891 6.021 1.464 1.464a1 1 0 0 1 .293.708v.171a1 1 0 0 1 -1 1h-9a1 1 0 0 0 -.625 1.781l10 8a1 1 0 0 0 .625.219h18a2 2 0 0 1 0 4z"/>
              <path class="fa-secondary" fill="currentColor" d="m5 44h2v4h-2z"/>
              <path class="fa-secondary" fill="currentColor" d="m14.049 19.219-1.229 3.781h-3.975a1 1 0 0 0 -.588 1.809l3.216 2.337-1.228 3.781a1 1 0 0 0 1.539 1.118l3.216-2.337 3.216 2.337a1 1 0 0 0 1.539-1.118l-1.228-3.781 3.216-2.337a1 1 0 0 0 -.588-1.809h-3.975l-1.229-3.781a1 1 0 0 0 -1.9 0zm2.404 5.781h1.625l-1.315.955a1 1 0 0 0 -.363 1.118l.5 1.545-1.314-.955a1 1 0 0 0 -1.176 0l-1.314.955.5-1.545a1 1 0 0 0 -.363-1.118l-1.311-.955h1.625a1 1 0 0 0 .951-.691l.5-1.545.5 1.545a1 1 0 0 0 .955.691z"/>
              <path class="fa-secondary" fill="currentColor" d="m21.473 13.146-1.228 3.781a1 1 0 0 0 1.539 1.118l3.216-2.337 3.216 2.337a1 1 0 0 0 1.539-1.118l-1.228-3.781 3.216-2.337a1 1 0 0 0 -.588-1.809h-3.975l-1.229-3.781a1 1 0 0 0 -1.9 0l-1.231 3.781h-3.975a1 1 0 0 0 -.588 1.809zm2.074-2.146a1 1 0 0 0 .951-.691l.502-1.545.5 1.545a1 1 0 0 0 .951.691h1.625l-1.315.955a1 1 0 0 0 -.363 1.118l.5 1.545-1.314-.955a1 1 0 0 0 -1.176 0l-1.314.955.5-1.545a1 1 0 0 0 -.363-1.118l-1.309-.955z"/>
              <path class="fa-secondary" fill="currentColor" d="m3.245 13.927a1 1 0 0 0 1.539 1.118l3.216-2.337 3.216 2.337a1 1 0 0 0 1.539-1.118l-1.228-3.781 3.216-2.337a1 1 0 0 0 -.588-1.809h-3.975l-1.229-3.781a1 1 0 0 0 -1.9 0l-1.231 3.781h-3.975a1 1 0 0 0 -.588 1.809l3.216 2.337zm3.302-5.927a1 1 0 0 0 .953-.691l.5-1.545.5 1.545a1 1 0 0 0 .953.691h1.625l-1.315.955a1 1 0 0 0 -.363 1.118l.5 1.545-1.314-.955a1 1 0 0 0 -1.176 0l-1.31.955.5-1.545a1 1 0 0 0 -.363-1.118l-1.315-.955z"/>
            </svg>
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Recommend</span>
          </a>
        </li>
        <!-- movie list button -->
        <li class="nav-item">
          <a @click="goMovie" class="nav-link" style="cursor:pointer">
            <svg 
              aria-hidden="true" 
              focusable="false" 
              data-prefix="fas" 
              data-icon="film" 
              class="svg-inline--fa fa-film fa-w-16" 
              role="img" 
              xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 512 512">
              <path 
              fill="currentColor" 
              d="M488 64h-8v20c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12V64H96v20c0 6.6-5.4 12-12 12H44c-6.6 0-12-5.4-12-12V64h-8C10.7 64 0 74.7 0 88v336c0 13.3 10.7 24 24 24h8v-20c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v20h320v-20c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v20h8c13.3 0 24-10.7 24-24V88c0-13.3-10.7-24-24-24zM96 372c0 6.6-5.4 12-12 12H44c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40zm0-96c0 6.6-5.4 12-12 12H44c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40zm0-96c0 6.6-5.4 12-12 12H44c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40zm272 208c0 6.6-5.4 12-12 12H156c-6.6 0-12-5.4-12-12v-96c0-6.6 5.4-12 12-12h200c6.6 0 12 5.4 12 12v96zm0-168c0 6.6-5.4 12-12 12H156c-6.6 0-12-5.4-12-12v-96c0-6.6 5.4-12 12-12h200c6.6 0 12 5.4 12 12v96zm112 152c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40zm0-96c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40zm0-96c0 6.6-5.4 12-12 12h-40c-6.6 0-12-5.4-12-12v-40c0-6.6 5.4-12 12-12h40c6.6 0 12 5.4 12 12v40z"
              class="fa-secondary"
              >
              </path>
            </svg>
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Movie</span>
          </a>
        </li>

       <!-- Login -->
        <li v-if="!isLoggedIn" class="nav-item" style="cursor:pointer" data-toggle="modal" data-target="#Login">
          <a class="nav-link">
            <svg 
              aria-hidden="true" 
              focusable="false" 
              data-prefix="fas" 
              data-icon="user-tie" 
              class="svg-inline--fa fa-user-tie fa-w-14" 
              role="img" 
              xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 448 512">
              <path 
                fill="currentColor" 
                d="M224 256c70.7 0 128-57.3 128-128S294.7 0 224 0 96 57.3 96 128s57.3 128 128 128zm95.8 32.6L272 480l-32-136 32-56h-96l32 56-32 136-47.8-191.4C56.9 292 0 350.3 0 422.4V464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48v-41.6c0-72.1-56.9-130.4-128.2-133.8z"
                class="fa-secondary"
                >
                </path>
              </svg>
            
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Login</span>
          </a>
        </li>

        <!-- profile -->
        <li v-if="isLoggedIn" class="nav-item">
          <a @click="goProfile" class="nav-link" style="cursor:pointer">
            <svg
              aria-hidden="true"
              focusable="false" 
              data-prefix="fas" 
              data-icon="user-circle" 
              class="svg-inline--fa fa-user-circle fa-w-16" 
              role="img" xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 496 512"
              >
              <path 
                fill="currentColor" 
                d="M248 8C111 8 0 119 0 256s111 248 248 248 248-111 248-248S385 8 248 8zm0 96c48.6 0 88 39.4 88 88s-39.4 88-88 88-88-39.4-88-88 39.4-88 88-88zm0 344c-58.7 0-111.3-26.6-146.5-68.2 18.8-35.4 55.6-59.8 98.5-59.8 2.4 0 4.8.4 7.1 1.1 13 4.2 26.6 6.9 40.9 6.9 14.3 0 28-2.7 40.9-6.9 2.3-.7 4.7-1.1 7.1-1.1 42.9 0 79.7 24.4 98.5 59.8C359.3 421.4 306.7 448 248 448z"
                class="fa-secondary"
                >
              </path>
            </svg>
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Profile</span>
          </a>
        </li>


        <!-- 로그아웃 -->
        <li v-if="isLoggedIn" class="nav-item" style="cursor:pointer" @click="logout">
          <a class="nav-link">
            <svg 
              aria-hidden="true" 
              focusable="false" 
              data-prefix="fas" 
              data-icon="user-slash" 
              class="svg-inline--fa fa-user-slash fa-w-20" 
              role="img" 
              xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 640 512"
              >
              <path 
                fill="currentColor" 
                d="M633.8 458.1L362.3 248.3C412.1 230.7 448 183.8 448 128 448 57.3 390.7 0 320 0c-67.1 0-121.5 51.8-126.9 117.4L45.5 3.4C38.5-2 28.5-.8 23 6.2L3.4 31.4c-5.4 7-4.2 17 2.8 22.4l588.4 454.7c7 5.4 17 4.2 22.5-2.8l19.6-25.3c5.4-6.8 4.1-16.9-2.9-22.3zM96 422.4V464c0 26.5 21.5 48 48 48h350.2L207.4 290.3C144.2 301.3 96 356 96 422.4z"
                class="fa-secondary"
                >
              </path>
            </svg>
            
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Logout</span>
          </a>
        </li>


        <li class="nav-item" id="themeButton" style="">
          <!-- <a class="nav-link"> -->
          <a class="">
            <!-- 화면 보호 모드 -->
            <svg
              class="theme-icon svg-inline--fa fa-sunglasses fa-w-18 fa-7x"
              id="solarIcon"
              aria-hidden="true"
              focusable="false"
              data-prefix="fad"
              data-icon="sunglasses"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 576 512"
            >
              <g class="fa-group">
                <path
                  fill="currentColor"
                  d="M574.09 280.38L528.75 98.66a87.94 87.94 0 0 0-113.19-62.14l-15.25 5.08a16 16 0 0 0-10.12 20.25L395.25 77a16 16 0 0 0 20.22 10.13l13.19-4.39c10.87-3.63 23-3.57 33.15 1.73a39.59 39.59 0 0 1 20.38 25.81l38.47 153.83a276.7 276.7 0 0 0-81.22-12.47c-34.75 0-74 7-114.85 26.75h-73.18c-40.85-19.75-80.07-26.75-114.85-26.75a276.75 276.75 0 0 0-81.22 12.45l38.47-153.8a39.61 39.61 0 0 1 20.38-25.82c10.15-5.29 22.28-5.34 33.15-1.73l13.16 4.39A16 16 0 0 0 180.75 77l5.06-15.19a16 16 0 0 0-10.12-20.21l-15.25-5.08A87.95 87.95 0 0 0 47.25 98.65L1.91 280.38A75.35 75.35 0 0 0 0 295.86v70.25C0 429 51.59 480 115.19 480h37.12c60.28 0 110.38-45.94 114.88-105.37l2.93-38.63h35.76l2.93 38.63c4.5 59.43 54.6 105.37 114.88 105.37h37.12C524.41 480 576 429 576 366.13v-70.25a62.67 62.67 0 0 0-1.91-15.5zM203.38 369.8c-2 25.9-24.41 46.2-51.07 46.2h-37.12C87 416 64 393.63 64 366.11v-37.55a217.35 217.35 0 0 1 72.59-12.9 196.51 196.51 0 0 1 69.91 12.9zM512 366.13c0 27.5-23 49.87-51.19 49.87h-37.12c-26.69 0-49.1-20.3-51.07-46.2l-3.12-41.24a196.55 196.55 0 0 1 69.94-12.9A217.41 217.41 0 0 1 512 328.58z"
                  class="fa-secondary"
                ></path>
                <path
                  fill="currentColor"
                  d="M64.19 367.9c0-.61-.19-1.18-.19-1.8 0 27.53 23 49.9 51.19 49.9h37.12c26.66 0 49.1-20.3 51.07-46.2l3.12-41.24c-14-5.29-28.31-8.38-42.78-10.42zm404-50l-95.83 47.91.3 4c2 25.9 24.38 46.2 51.07 46.2h37.12C489 416 512 393.63 512 366.13v-37.55a227.76 227.76 0 0 0-43.85-10.66z"
                  class="fa-primary"
                ></path>
              </g>
            </svg>
            <!-- 주간 모드 -->
            <svg
              class="theme-icon svg-inline--fa fa-sun fa-w-16 fa-7x"
              id="lightIcon"
              aria-hidden="true"
              focusable="false"
              data-prefix="fad"
              data-icon="sun"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 512 512"
            >
              <g class="fa-group">
                <path
                  fill="currentColor"
                  d="M502.42 240.5l-94.7-47.3 33.5-100.4c4.5-13.6-8.4-26.5-21.9-21.9l-100.4 33.5-47.41-94.8a17.31 17.31 0 0 0-31 0l-47.3 94.7L92.7 70.8c-13.6-4.5-26.5 8.4-21.9 21.9l33.5 100.4-94.7 47.4a17.31 17.31 0 0 0 0 31l94.7 47.3-33.5 100.5c-4.5 13.6 8.4 26.5 21.9 21.9l100.41-33.5 47.3 94.7a17.31 17.31 0 0 0 31 0l47.31-94.7 100.4 33.5c13.6 4.5 26.5-8.4 21.9-21.9l-33.5-100.4 94.7-47.3a17.33 17.33 0 0 0 .2-31.1zm-155.9 106c-49.91 49.9-131.11 49.9-181 0a128.13 128.13 0 0 1 0-181c49.9-49.9 131.1-49.9 181 0a128.13 128.13 0 0 1 0 181z"
                  class="fa-secondary"
                ></path>
                <path
                  fill="currentColor"
                  d="M352 256a96 96 0 1 1-96-96 96.15 96.15 0 0 1 96 96z"
                  class="fa-primary"
                ></path>
              </g>
            </svg>
            <!-- 야간모드 -->
            <svg
              class="theme-icon svg-inline--fa fa-moon-stars fa-w-16 fa-7x"
              id="darkIcon"
              aria-hidden="true"
              focusable="false"
              data-prefix="fad"
              data-icon="moon-stars"
              role="img"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 512 512"
            >
              <g class="fa-group">
                <path
                  fill="currentColor"
                  d="M320 32L304 0l-16 32-32 16 32 16 16 32 16-32 32-16zm138.7 149.3L432 128l-26.7 53.3L352 208l53.3 26.7L432 288l26.7-53.3L512 208z"
                  class="fa-secondary"
                ></path>
                <path
                  fill="currentColor"
                  d="M332.2 426.4c8.1-1.6 13.9 8 8.6 14.5a191.18 191.18 0 0 1-149 71.1C85.8 512 0 426 0 320c0-120 108.7-210.6 227-188.8 8.2 1.6 10.1 12.6 2.8 16.7a150.3 150.3 0 0 0-76.1 130.8c0 94 85.4 165.4 178.5 147.7z"
                  class="fa-primary"
                ></path>
              </g>
            </svg>
            
            <!-- <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;">Themify</span> -->
            <span class="link-text" style="font-family: 'Black Han Sans', sans-serif;"></span>
          </a>
        </li>
      </ul>
    </nav>

  </div>
</template>

<script>

import axios from "axios";
import constants from '../lib/constants'
import Swal from 'sweetalert2';
export default {
  data() {
    return {
      collapseflag: false,
      isLoggedIn : false,
    }
  },
  created(){
    this.user_check()
  },
  updated(){
    this.user_check()
  },
  props: {
    isHeader: Boolean,
  },
  methods: {
    user_check(){
      if (this.$cookies.isKey('auth-token')){
        this.isLoggedIn = true
      }
      else{
        this.isLoggedIn = false
      }
    },
    logout() {
      const axiosConfig ={
        headers:{
          Authorization : `Token ${this.$cookies.get('auth-token')}`
        },
      }
      axios.post(constants.SERVER_URL + '/rest-auth/logout/',null,axiosConfig)
      .then(()=>{
        this.$cookies.remove('auth-token')
        this.isLoggedIn=false
        setTimeout(() => {
          this.$router.push({name:constants.URL_TYPE.MAIN}).catch(()=>{this.$router.go()})
        },1200)
        const Toast = Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 1000,
          timerProgressBar: true,
        })

        Toast.fire({
          icon: 'success',
          title: '로그아웃 되었습니다.'
        })
      })
      .catch((error)=>{
        console.log(error.response.data)
      })
    },
    goMain() {
      this.$router.push('/').catch(() => {
        this.$router.go()
      })
    },
    goMovie() {
      this.$router.push('/movie').catch(() => {
        this.$router.go()
      })
    },
    goRecommend() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(constants.SERVER_URL+`/accounts/rating-check/`,config)
        .then((res)=>{
          console.log(res.data)
          if(res.data){
            this.$router.push('/movierecommend').catch(() => {
              this.$router.go()
            })
          }else{
            alert("평가한 영화가 10개 이상이어야 추천이 가능합니다.")
          }
        })
      
    },
    goProfile() {
      this.$router.push('/user/profile').catch(() => {
        this.$router.go()
      })
    },
  }
}
  
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Kufam:wght@800&display=swap');

:root {
  /* font-size: 16px; */
  /* font-family: 'Black Han Sans', sans-serif; */
  --text-primary: #b6b6b6;
  --text-secondary: #ececec;
  --bg-primary: #23232e;
  --bg-secondary: #141418;
  --transition-speed: 600ms;
}

.body {
  color: black;
  background-color: white;
  margin: 0;
  padding: 0;
}

.body::-webkit-scrollbar {
  width: 0.25rem;
}

.body::-webkit-scrollbar-track {
  background: #1e1e24;
  /* background: black; */
}

.body::-webkit-scrollbar-thumb {
  background: #e63c12;
}

/* main {
  margin-left: 5rem;
  padding: 1rem;
} */

.navbar {
  position: fixed;
  background-color: var(--bg-primary);
  transition: width 600ms ease;
  overflow: scroll;
  padding: 0;
}

.navbar-nav {
  /* list-style: none; */
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}

.nav-item {
  width: 100%;
}

.nav-item:last-child {
  margin-top: auto;
}

.nav-link {
  display: flex;
  align-items: center;
  height: 5rem;
  color: var(--text-primary);
  text-decoration: none;
  filter: grayscale(100%) opacity(0.7);
  transition: var(--transition-speed);
}

.nav-link:hover {
  filter: grayscale(0%) opacity(1);
  background: var(--bg-secondary);
  color: var(--text-secondary);
}

.link-text {
  display: none;
  margin-left: 1rem;
}

.nav-link svg {
  width: 1rem;
  min-width: 2rem;
  margin: 0 1.5rem;
}

.fa-primary {
  color: #ff7eee;
}

.fa-secondary {
  color: #f53b1a;
}

.fa-primary,
.fa-secondary {
  transition: var(--transition-speed);
}

.logo {
  font-weight: bold;
  text-transform: uppercase;
  margin-bottom: 0rem;
  text-align: center;
  color: var(--text-secondary);
  background: var(--bg-secondary);
  font-size: 1.5rem;
  letter-spacing: 0.3ch;
  width: 100%;
}

.logo svg {
  transform: rotate(0deg);
  transition: var(--transition-speed);
}

.logo-text
{
  display: inline;
  position: absolute;
  left: -999px;
  transition: var(--transition-speed);
}

.navbar:hover .logo svg {
  transform: rotate(-180deg);
}

/* Small screens */
@media only screen and (max-width: 600px) {
  .navbar {
    bottom: 0;
    width: 100vw;
    height: 5rem;
  }

  .logo {
    display: none;
  }

  .navbar-nav {
    flex-direction: row;
  }

  .nav-link {
    justify-content: center;
  }

  /* main {
    margin: 0;
  } */
}

/* Large screens */
@media only screen and (min-width: 600px) {
  .navbar {
    top: 0;
    width: 5rem;
    height: 100vh;
  }

  .navbar:hover {
    width: 16rem;
  }

  .navbar:hover .link-text {
    display: inline;
  }

  .navbar:hover .logo svg
  {
    margin-left: 11rem;
  }

  .navbar:hover .logo-text
  {
    left: 0px;
  }
}

.dark {
  --text-primary: #b6b6b6;
  --text-secondary: #ececec;
  --bg-primary: #23232e;
  --bg-secondary: #141418;
}

.light {
  --text-primary: #1f1f1f;
  --text-secondary: #000000;
  --bg-primary: #ffffff;
  --bg-secondary: #e4e4e4;
}

.solar {
  --text-primary: #576e75;
  --text-secondary: #35535c;
  --bg-primary: #fdf6e3;
  --bg-secondary: #f5e5b8;
}

.theme-icon {
  display: none;
}

.dark #darkIcon {
  display: block;
}

.light #lightIcon {
  display: block;
}

.solar #solarIcon {
  display: block;
}
</style>