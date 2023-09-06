<script lang="ts">
  let inputText: String = "";
  let outputText: String = "";
  async function summarizeText() {
    console.log(inputText);
    outputText = inputText;
    const response = await fetch(
      "https://us-central1-cv3-serverless-web-apis.cloudfunctions.net/vertex-ai-test",
      {
        method: "POST",
        body:JSON.stringify(inputText),
      }
    );
    console.log(response);
  }
</script>

<div class="bg-gray-100">
  <div class="bg-blue-600 text-white p-4 shadow-lg font-bold text-3xl">
    Vertex Summarizer
  </div>
  <div class="flex flex-row m-16 justify-between h-screen">
    <textarea
      name=""
      id=""
      class="w-2/6 h-1/2 text-xl font-mono"
      bind:value={inputText}
    />
    <button
      on:click={summarizeText}
      class="bg-blue-600 text-white font-bold text-xl h-fit p-4 rounded-lg"
    >
      Summarize
    </button>
    <textarea
      name=""
      id=""
      class="w-2/6 h-1/2 text-xl font-mono"
      bind:value={outputText}
      readOnly
    />
  </div>
</div>
