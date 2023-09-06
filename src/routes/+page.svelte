<script lang="ts">
  import { PUBLIC_FUNCTION_URL } from "$env/static/public";
  import TextareaComponent from "$lib/textarea-component.svelte";
  let inputText: String = "";
  let outputText: String = "";
  let loadingState: boolean = false;
  async function summarizeText() {
    loadingState = true;
    console.log(inputText);
    const response = await fetch(PUBLIC_FUNCTION_URL, {
      method: "POST",
      body: JSON.stringify(inputText),
    });
    outputText = await response.text();
    loadingState = false;
  }
</script>

<div class="bg-gray-100 min-h-screen">
  <!-- navbar  -->
  <div
    class="flex flex-row items-center space-x-4 bg-blue-600 text-white p-4 shadow-lg font-bold text-3xl mb-4 lg:mb-16"
  >
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
      <button
        on:click={summarizeText}
        class="bg-blue-600 hover:scale-105 transition text-white font-bold text-xl h-fit p-4 rounded-lg"
      >
        {loadingState ? "Processing" : "Summarize"}
      </button>
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
    <a href="https://github.com/bhaaratkrishnan/vertex-summarizer-svelte" target="_blank">
      <div>Made by Bhaarat Krishnan</div>
    </a>
  </div>
</div>
