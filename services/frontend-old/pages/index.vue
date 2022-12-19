<template>
  <div id="conditional-section">
    <button id="messageBtn">Hide message</button>
    <p id="message">Hello world</p>
  </div>
</template>

<script type="text/javascript">
  $(document).ready(() => {
    const $btn = $("#messageBtn");
    const $message = $("#message");
    $btn.click(() => {      
      const isVisible = $message.is(":visible");
      if (isVisible) {
        $message.hide();
        $btn.text("Show message");
      } else {
        $message.show();
        $btn.text("Hide message");
      }
    });
  });
</script>
