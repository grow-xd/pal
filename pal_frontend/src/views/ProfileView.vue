<template>
  <div class="bg-[url('../assets/img5.jpg')] rounded-xl m-2 shadow-xl duration-700 p-2">
    <div class="flex flex-row rounded-lg border border-gray-200/80 bg-white p-6 m-3">
      <div class="relative">
        <img class="w-40 h-40 rounded-md object-cover" src="https://api.lorem.space/image/face?w=150&h=150" alt="User" />
      </div>

      <!-- Meta Body -->
      <div class="flex flex-col px-6">
        <!-- Username Container -->
        <div class="flex h-8 flex-row">
          <!-- Username -->
          <a href="" target="_blank">
            <h2 class="text-lg font-semibold">{{ name }}</h2>
          </a>

          <!-- User Verified -->
          <svg class="my-auto ml-2 h-5 fill-blue-400" xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="24" height="24" viewBox="0 0 24 24">
            <path
              d="M23,12L20.56,9.22L20.9,5.54L17.29,4.72L15.4,1.54L12,3L8.6,1.54L6.71,4.72L3.1,5.53L3.44,9.21L1,12L3.44,14.78L3.1,18.47L6.71,19.29L8.6,22.47L12,21L15.4,22.46L17.29,19.28L20.9,18.46L20.56,14.78L23,12M10,17L6,13L7.41,11.59L10,14.17L16.59,7.58L18,9L10,17Z" />
          </svg>
        </div>

        <!-- Meta Badges -->
        <div class="my-2 flex flex-row space-x-2">
          <!-- Badge Role -->
          <div class="flex flex-row">
            <svg class="mr-2 h-4 w-4 fill-gray-500/80" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
              stroke-width="1.5" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M18 18.72a9.094 9.094 0 003.741-.479 3 3 0 00-4.682-2.72m.94 3.198l.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0112 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 016 18.719m12 0a5.971 5.971 0 00-.941-3.197m0 0A5.995 5.995 0 0012 12.75a5.995 5.995 0 00-5.058 2.772m0 0a3 3 0 00-4.681 2.72 8.986 8.986 0 003.74.477m.94-3.197a5.971 5.971 0 00-.94 3.197M15 6.75a3 3 0 11-6 0 3 3 0 016 0zm6 3a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0zm-13.5 0a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0z" />
            </svg>

            <div class="text-xs text-gray-400/80 hover:text-gray-400">
              {{ username }}
            </div>
          </div>

          <!-- Badge Location -->
          <div class="flex flex-row">
            <svg class="mr-2 h-4 w-4 fill-gray-500/80" xmlns="http://www.w3.org/2000/svg"
              xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="24" height="24" viewBox="0 0 24 24">
              <path
                d="M12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5M12,2A7,7 0 0,1 19,9C19,14.25 12,22 12,22C12,22 5,14.25 5,9A7,7 0 0,1 12,2M12,4A5,5 0 0,0 7,9C7,10 7,12 12,18.71C17,12 17,10 17,9A5,5 0 0,0 12,4Z" />
            </svg>

            <div class="text-xs text-gray-400/80 hover:text-gray-400">
              {{ location }}
            </div>
          </div>

          <!-- Badge Email-->
        </div>

        <!-- Mini Cards -->
        <div class="mt-2 flex flex-row items-center space-x-5">
          <!-- Comments -->
          <a href="#"
            class="flex h-20 w-40 flex-col items-center justify-center rounded-md border border-dashed border-gray-200 transition-colors duration-100 ease-in-out hover:border-gray-400/80">
            <div class="flex flex-row items-center justify-center">
              <svg class="mr-3 fill-gray-500/95" xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="24" height="24" viewBox="0 0 24 24">
                <path
                  d="M12,23A1,1 0 0,1 11,22V19H7A2,2 0 0,1 5,17V7A2,2 0 0,1 7,5H21A2,2 0 0,1 23,7V17A2,2 0 0,1 21,19H16.9L13.2,22.71C13,22.89 12.76,23 12.5,23H12M13,17V20.08L16.08,17H21V7H7V17H13M3,15H1V3A2,2 0 0,1 3,1H19V3H3V15M9,9H19V11H9V9M9,13H17V15H9V13Z" />
              </svg>

              <span class="font-bold text-gray-600"> {{ groups.length }} </span>
            </div>

            <div class="mt-2 text-sm text-gray-400">Communities</div>
          </a>

          <!-- Projects -->
          <a href="#"
            class="flex h-20 w-40 flex-col items-center justify-center rounded-md border border-dashed border-gray-200 transition-colors duration-100 ease-in-out hover:border-gray-400/80">
            <div class="flex flex-row items-center justify-center">
              <svg class="mr-3 fill-gray-500/95" xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="24" height="24" viewBox="0 0 24 24">
                <path
                  d="M2.5 19.6L3.8 20.2V11.2L1.4 17C1 18.1 1.5 19.2 2.5 19.6M15.2 4.8L20.2 16.8L12.9 19.8L7.9 7.9V7.8L15.2 4.8M15.3 2.8C15 2.8 14.8 2.8 14.5 2.9L7.1 6C6.4 6.3 5.9 7 5.9 7.8C5.9 8 5.9 8.3 6 8.6L11 20.5C11.3 21.3 12 21.7 12.8 21.7C13.1 21.7 13.3 21.7 13.6 21.6L21 18.5C22 18.1 22.5 16.9 22.1 15.9L17.1 4C16.8 3.2 16 2.8 15.3 2.8M10.5 9.9C9.9 9.9 9.5 9.5 9.5 8.9S9.9 7.9 10.5 7.9C11.1 7.9 11.5 8.4 11.5 8.9S11.1 9.9 10.5 9.9M5.9 19.8C5.9 20.9 6.8 21.8 7.9 21.8H9.3L5.9 13.5V19.8Z" />
              </svg>

              <span class="font-bold text-gray-600">
                {{ friends.length }}
              </span>
            </div>

            <div class="mt-2 text-sm text-gray-400">Friends</div>
          </a>
        </div>
      </div>

      <!-- Right Actions Container -->
      <div class="w-100 flex flex-grow flex-col items-end justify-start">
        <div class="flex flex-row space-x-3">
          <!-- Follow Button -->
          <button
            class="flex rounded-md bg-blue-500 py-2 px-4 text-white transition-all duration-150 ease-in-out hover:bg-blue-600"
            type="button" data-modal-toggle="default-modal">
            Update Location
          </button>
        </div>
      </div>
    </div>

    <div id="default-modal" data-modal-show="true" aria-hidden="true"
      class="hidden overflow-x-hidden overflow-y-auto fixed h-modal md:h-full top-4 left-0 right-0 md:inset-0 z-50 justify-center items-center">
      <div class="relative w-full max-w-2xl px-4 h-full md:h-auto">
        <!-- Modal content -->
        <div class="bg-white rounded-lg shadow relative dark:bg-gray-700">
          <!-- Modal header -->
          <div class="flex items-start justify-between p-5 border-b rounded-t dark:border-gray-600">
            <h3 class="text-gray-900 text-xl lg:text-2xl font-semibold dark:text-white">
              Enter New Location
            </h3>
            <button type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
              data-modal-toggle="default-modal">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"></path>
              </svg>
            </button>
          </div>
          <!-- Modal body -->
          <div class="p-6 space-y-4">
            <label class="block font-semibold text-white"> New Location</label>
            <input type="text" v-model="nloc" placeholder="Enter new location"
              class="border w-full h-5 px-3 py-5 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md">

              <label class="block font-semibold text-white"> Arrival Date</label>
            <input type="date" v-model="adate" placeholder="Username"
              class="border w-full h-5 px-3 py-5 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md">

              <label class="block font-semibold text-white"> Departure Date</label>
            <input type="date" v-model="ddate" placeholder="Username"
              class="border w-full h-5 px-3 py-5 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md">

              <label class="block font-semibold text-white"> When you are not free..?</label>
            <input type="text" v-model="nfdates" placeholder="When you are not free?"
              class="border w-full h-5 px-3 py-5 hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md">
            
          </div>
          <!-- Modal footer -->
          <div class="flex space-x-2 items-center p-6 border-t border-gray-200 rounded-b dark:border-gray-600">
            <button data-modal-toggle="default-modal" type="button" @click="updateloc"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
              Update
            </button>

          </div>
        </div>
      </div>
    </div>

    <div class="flex flex-row justify-center h-screen items-center">
      <div class="grid bg-blue-600 text-xl h-2/3 w-2/3 text-white text-center m-2 p-2 rounded-xl place-content-center">
        <div class="text-center text-2xl underline font-bold text-white p-4">
          Your Friends
        </div>
        <div class="overflow-y grid grid-cols-3 md:grid-cols-5 duration-700">
          <div v-for="group in friends" v-bind:key="group.id">
            <div
              class="bg-blue-100 col-span-1 shadow-xl rounded-xl text-center p-2 m-1 text-sm md:text-lg text-black hover-trigger duration-700">
              <div
                class="absolute bg-white border rounded-xl border-grey-100 px-4 py-2 hover-target duration-700 divide-y divide-double">
                <div>Username: {{ group.username }}</div>
                <div>Location: {{ group.location }}</div>
              </div>
              {{ group.name }}
            </div>
          </div>
        </div>

        <hr class="my-12 h-0.5 border-t-0 bg-neutral-100 opacity-100 dark:opacity-50 m-6 mt-20" />

        <div class="text-center text-2xl underline font-bold text-white p-4">
          Your Communities
        </div>
        <div class="overflow-y grid grid-cols-3 md:grid-cols-5 duration-700 align-middle">
          <div v-for="group in groups" v-bind:key="group.id">
            <div
              class="bg-blue-100 col-span-1 shadow-xl rounded-xl text-center p-2 m-1 text-sm md:text-lg text-black hover-trigger duration-700">
              <div
                class="absolute bg-white border rounded-xl border-grey-100 px-4 py-2 hover-target duration-700 divide-y divide-double">
                <div>Commun Code: {{ group.unique_code }}</div>
                <div>Members: {{ group.members.length }}</div>
              </div>
              {{ group.name }}
            </div>
          </div>
        </div>
      </div>

      <div
        class="grid bg-blue-600 text-xl h-2/3 w-2/3 text-white text-center m-2 p-2 rounded-xl duration-700 place-content-center">
        <label class="block mt-3 font-semibold no-underline">
          Add a new friend
        </label>
        <input type="text" v-model="frndName" placeholder="Friend Username"
          class="border h-5 text-black px-3 py-5 mt-2 justify-center hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md" />
        <button type="submit" @click="addfriend"
          class="m-2 bg-purple-500 text-white py-1 px-3 rounded-md hover:bg-purple-600 ">
          Add Friend
        </button>

        <hr class="my-12 h-0.5 border-t-0 bg-neutral-100 opacity-100 dark:opacity-50 m-6 mt-20" />
        <div class="flex flex-col md:flex-row justify-between gap-2">
          <div>
            <label class="block mt-3 font-semibold no-underline">
              Join Community
            </label>
            <input type="text" v-model="joinName" placeholder="Community Unique Code"
              class="border h-5 text-black px-3 py-5 mt-2 justify-center hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md" />
            <button type="submit" @click="joingroup"
              class="m-2 bg-purple-500 text-white py-1 px-3 rounded-md hover:bg-purple-600">
              Join
            </button>
          </div>
          <div>
            <label class="block mt-3 font-semibold no-underline">
              Create Community
            </label>
            <input type="text" v-model="createName" placeholder="Community Name"
              class="border h-5 text-black px-3 py-5 mt-2 justify-center hover:outline-none focus:outline-none focus:ring-indigo-500 focus:ring-1 rounded-md" />
            <button type="submit" @click="createGroup"
              class="m-2 bg-purple-500 text-white py-1 px-3 rounded-md hover:bg-purple-600">
              Create
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.hover-trigger .hover-target {
  display: none;
}

.hover-trigger:hover .hover-target {
  display: block;
}
</style>

<script>
import { useToast } from "vue-toastification";

export default {
  setup() {
    // Get toast interface
    const toast = useToast();

    return { toast };
  },
  data() {
    return {
      id: "",
      username: "",
      name: "",
      location: "",
      friends: [],
      frndName: "",
      joinName: "",
      createName: "",
      groups: [],
      nloc:'',
      adate:'',
      ddate:'',
      nfdates:''
    };
  },
  created() {
    this.getInfo();
    this.getgroups();
  },

  methods: {
    getInfo() {
      const token = localStorage.getItem("token");

      const requestOptions = {
        method: "GET",
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      };

      fetch("http://localhost:8000/api/get_user_info/", requestOptions)
        .then((result) => result.json())
        .then((response) => {
          console.log(response);

          this.id = response.id;
          this.name = response.name;
          this.username = response.username;
          this.location = response.location;

          this.getfriends();
        });
    },

    getfriends() {
      const token = localStorage.getItem("token");

      const requestOptions = {
        method: "GET",
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      };

      fetch(
        `http://localhost:8000/api/userprofiles/${this.id}/friends/`,
        requestOptions
      )
        .then((result) => result.json())
        .then((response) => {
          console.log(response);

          this.friends = response;
        });
    },

    getgroups() {
      const token = localStorage.getItem("token");

      const requestOptions = {
        method: "GET",
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      };

      fetch(`http://localhost:8000/api/groups/all/`, requestOptions)
        .then((result) => result.json())
        .then((response) => {
          console.log(response);

          this.groups = response;
        });
    },

    addfriend(e) {
      e.preventDefault();

      const token = localStorage.getItem("token");

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      };

      fetch(
        `http://localhost:8000/api/add_friend/${this.frndName}/`,
        requestOptions
      )
        .then((result) => result.json())
        .then((response) => {
          console.log(response);
          this.toast.info(response.detail);
          this.getfriends();
        });
    },

    updateloc(e) {
      e.preventDefault();

      const token = localStorage.getItem("token");

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({ location: this.nloc, arrival_date: this.adate,  departure_date: this.ddate, available_dates: this.nfdates})
        
      };

      fetch(
        `http://localhost:8000/api/travel/update-travel/`,
        requestOptions
      )
        .then((result) => result.json())
        .then((response) => {
          console.log(response);
          this.toast.info(response.detail);
        });
    },

    joingroup(e) {
      e.preventDefault();

      if (!this.joinName.length) {
        alert("enter Group Code");
        return;
      }

      const token = localStorage.getItem("token");

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ unique_code: this.joinName }),
      };

      fetch(`http://localhost:8000/api/groups/join/`, requestOptions)
        .then((result) => result.json())
        .then((response) => {
          console.log(response);
          this.toast.info(response.detail);
        });
    },
    createGroup(e) {
      e.preventDefault();

      const token = localStorage.getItem("token");

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ name: this.createName }),
      };

      fetch(`http://localhost:8000/api/groups/create/ `, requestOptions)
        .then((result) => result.json())
        .then((response) => {
          console.log(response);
          this.toast.info(response.detail);
        });
    },
  },
};
</script>
