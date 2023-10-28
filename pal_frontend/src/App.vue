<template>
  <!-- component -->
  <div>
    <div class="sticky top-0 z-50">
      <div>
        <div class="w-full bg-black opacity-80 h-20 flex justify-between">
          <div class="w-full lg:w-30/6 xl:w-full h-full flex items-center px-4">
            <img
              class="rounded-lg bg-white w-32"
              src="../logo.png"
              alt="addify logo"
            />
          </div>

          <div class="w-full h-full flex justify-end items-center">
            <button class="bg-black text-white rounded-xl hover:bg-gray-800 p-2 m-2 mr-7">SignIn</button>
          </div>
        </div>
      </div>
    </div>

    <div class="text-7xl text-center">Pal app</div>

    <aside
      class="relative overflow-hidden text-black rounded-lg sm:mx-16 mx-2 sm:py-16"
    >
      <div
        class="relative z-10 max-w-screen-xl px-4 pb-20 pt-10 sm:py-24 mx-auto sm:px-6 lg:px-8"
      >
        <div
          class="max-w-xl sm:mt-1 mt-80 space-y-8 text-center sm:text-right sm:ml-auto"
        >
          <h2 class="text-4xl font-bold sm:text-5xl">
            Lorem Ipsum
            <span class="hidden sm:block text-4xl"> Lorem Ipsum </span>
          </h2>

          <a
            class="inline-flex text-white items-center px-6 py-3 font-medium bg-rose-500 rounded-lg hover:opacity-75"
            href=""
          >
            
            
            &nbsp; Register
          </a>
        </div>
      </div>

      <div class="absolute inset-0 w-full sm:my-20 sm:pt-1 pt-12 h-full">
        <img class="w-2/3" src="../friends.png" />
      </div>
    </aside>

    

    <footer class="text-center">
      <hr />
      <p class="text-center py-5">
        Crafted with ❤️ Tech Agents
        <span class="font-black"
          ><Link href="https://twitter.com/sahilnetic">@sahilnetic</Link></span
        >
      </p>
    </footer>
  </div>
</template>
