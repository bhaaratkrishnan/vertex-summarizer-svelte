<script lang="ts">
  export let name:String;
  export let placeholder:string="";
  export let text: String;
  export let readOnly: boolean = false;
</script>

<div class="flex flex-col lg:w-2/6">
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
