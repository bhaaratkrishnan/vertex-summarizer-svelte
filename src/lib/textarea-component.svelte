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
  // input value binding variables 
  export let name:String;
  export let placeholder:string="";
  export let text: String;
  export let readOnly: boolean = false;
</script>

<div class="flex flex-col lg:w-2/6">
  <!-- textarea -->
  <label for="text" class="text-xl my-4">{name}</label>
  <textarea
    name="text"
    id=""
    placeholder={placeholder}
    class="text-xl font-mono p-4 rounded-lg lg:h-96 h-48"
    bind:value={text}
    readonly={readOnly}
  />
</div>
