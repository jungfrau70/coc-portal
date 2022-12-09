<template>
  <!-- Modal -->
  <div
    id="exampleModal"
    class="modal fade"
    tabindex="-1"
    role="dialog"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 id="exampleModalLabel" class="modal-title">Modal title</h5>
          <v-btn
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </v-btn>
        </div>
        <div class="modal-body">hihi</div>
        <div class="modal-footer">
          <v-btn type="button" class="btn btn-secondary" data-dismiss="modal">
            Close
          </v-btn>
          <v-btn type="button" class="btn btn-primary">Save changes</v-btn>
        </div>
      </div>
    </div>
  </div>
</template>
