
<template>
    <div class="bg-blue-700 h-screen rounded-xl m-2">
        <div class="text-center text-7xl font-bold p-20 text-white">
            Welcome, Rishabh
        </div>
        <div class="flex flex-cols justify-center">
            <div class="text-center text-2xl font-bold p-4 text-white">
                Your current location: location
            </div>
            <button class="  text-green-500 hover:font-bold duration-800 font-semibold underline p-1">
                Change Location
            </button>
        </div>

        <hr class="my-12 h-0.5 border-t-0 bg-neutral-100 opacity-100 dark:opacity-50 m-6 mt-20" />

        <div class="grid grid-cols-2 divide-x pt-6 ">


            <div class="col-span-1 min-h-screen items-center justify-center">

                <div class=" text-center text-2xl underline font-bold text-white p-4">
                    <br>
                    Friends in your area

                </div>

                <div class="flex justify-items-center justify-center m-2">
                    
                    <div class="text-lg bg-white shadow-xl rounded-xl w-2/3 text-black p-2">
                            hii
                        </div>


                </div>

            </div>

            <div class="col-span-1">
                <div class=" text-center text-2xl underline font-bold text-white p-4">
                    Communities members in your area
                </div>
                <div class="flex justify-items-center justify-center m-2">
                    
                    <div class="flex justify-between text-lg bg-white shadow-xl rounded-xl w-2/3 text-black p-2">
                            <div class="text-lg font-bold">name</div>
                            <div class="text-lg">community</div>
                        </div>

                </div>
            </div>
        </div>
    </div>
</template>

