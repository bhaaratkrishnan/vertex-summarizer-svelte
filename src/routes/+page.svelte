<!-- Copyright 2022 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    https://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. -->


<script lang="ts">
  // cloud function url imported from env variables 
  import { PUBLIC_FUNCTION_URL } from "$env/static/public";
  // textarea component 
  import TextareaComponent from "$lib/textarea-component.svelte";
  // textarea binding variables 
  let inputText: String = "";
  let outputText: String = "";
  // loading state indication 
  let loadingState: boolean = false;
  // variable for reading .txt files
  let file: HTMLInputElement;
  // function to send HTTP request cloud function and recieve summary 
  async function summarizeText() {
    loadingState = true;
    const response = await fetch(PUBLIC_FUNCTION_URL, {
      method: "POST",
      body: JSON.stringify(inputText),
    });
    outputText = await response.text();
    loadingState = false;
  }
  // function for reading .txt files and storing it in variable 
  async function fileUpload() {
    if (file.files !== null) {
      // inputText = await file.files[0].text();
      inputText = await file.files[0].text();
    }
  }
</script>

<!-- head  -->
<svelte:head>
  <title>Vertex Summarizer</title>
</svelte:head>

<div class="bg-gray-100 min-h-screen">
  <!-- navbar  -->
  <div
    class="flex flex-row items-center space-x-4 bg-blue-600 text-white p-4 shadow-lg font-bold text-3xl mb-4 lg:mb-16"
  >
    <!-- google cloud logo  -->
    <img
      class="w-8 h-8"
      src="https://www.gend.co/hs-fs/hubfs/gcp-logo-cloud.png?width=730&name=gcp-logo-cloud.png"
      alt=""
    />
    <div>Vertex Summarizer</div>
  </div>
  <!-- article summarizer  -->
  <div
    class="flex flex-col lg:flex-row mx-4 space-y-6 lg:space-y-0 lg:mx-16 lg:justify-between"
  >
    <!-- input textarea  -->
    <TextareaComponent
      bind:text={inputText}
      name="Original Text"
      placeholder="Enter Text"
    />
    <!-- stats area  -->
    <div class="flex flex-col space-y-8 items-center justify-center">
      <!-- summarize button  -->
      <button
        disabled={loadingState}
        on:click={summarizeText}
        class="bg-blue-600 hover:scale-105 transition text-white font-bold text-xl h-fit p-4 rounded-lg"
      >
        {loadingState ? "Processing" : "Summarize"}
      </button>
      <!-- file input  -->
      <label
        for="upload-file"
        class="bg-blue-600 cursor-pointer p-4 rounded-lg hover:scale-105 transition ease-in-out text-xl font-bold text-white"
        >Upload File (.txt)</label
      >
      <input
        id="upload-file"
        type="file"
        accept=".txt"
        on:change={fileUpload}
        bind:this={file}
        hidden
      />
      <!-- input characters  -->
      <div
        class="text-xl hover:scale-105 transition font-bold text-center bg-white text-blue-600 p-4 rounded-lg"
      >
        Original Characters <br />
        {inputText.length}
      </div>
      <!-- output characters  -->
      <div
        class="text-xl hover:scale-105 transition font-bold text-center bg-white text-blue-600 p-4 rounded-lg"
      >
        Summarized Characters <br />
        {outputText.length}
      </div>
    </div>
    <!-- output textarea  -->
    <TextareaComponent bind:text={outputText} name="Summary" readOnly />
  </div>
  <!-- footer  -->
  <div
    class="bg-blue-600 flex-row flex text-white p-4 shadow-lg text-xl mt-4 lg:mt-16 sticky top-[100vh]"
  >
    <a
      href="https://github.com/bhaaratkrishnan/vertex-summarizer-svelte"
      target="_blank"
    >
      <div>Made by Bhaarat Krishnan</div>
    </a>
  </div>
</div>
