<template lang="">
  <div>
    <v-row>
      <v-col>
        <p>년</p>
        <select v-model="year" class="select selected selected-value">
          <option
            v-for="(option, index) in years"
            :key="index"
            :value="option.value"
          >
            {{ option.text }}
          </option>
        </select>
      </v-col>
      <v-col>
        <p>월</p>
        <select v-model="month" class="select selected selected-value">
          <option
            v-for="(option, index) in months"
            :key="index"
            :value="option.value"
          >
            {{ option.text }}
          </option>
        </select>
      </v-col>
      <v-col>
        <p>리전</p>
        <select v-model="region" class="select selected selected-value">
          <option
            v-for="(option, index) in regions"
            :key="index"
            :value="option.value"
          >
            {{ option.text }}
          </option>
        </select>
      </v-col>    
      <v-col>
        <p>AZ</p>
        <select v-model="AZ" class="select selected selected-value">
          <option
            v-for="(option, index) in AZs"
            :key="index"
            :value="option.value"
          >
            {{ option.text }}
          </option>
        </select>
      </v-col>   
      <v-col>
        <p>테넌트</p>
        <select v-model="tenant" class="select selected selected-value">
          <option
            v-for="(option, index) in tenants"
            :key="index"
            :value="option.value"
          >
            {{ option.text }}
          </option>
        </select>
      </v-col>   
      <v-col>
        <p>상태</p>
        <select v-model="status" class="select selected selected-value">
          <option
            v-for="(option, index) in status"
            :key="index"
            :value="option.value"
          >
            {{ option.text }}
          </option>
        </select>
      </v-col>     
    </v-row>
    <v-row>
      <h1>{{year}}년 {{month}}월</h1>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      year: '2022',
      years: [
        { text: '2022', value: '2022' },
        { text: '2023', value: '2023' },
      ],
      month: '1',
      months: [
        { text: 'Jan', value: '1' },
        { text: 'Feb', value: '2' },
        { text: 'Mar', value: '3' },
        { text: 'Apr', value: '4' },
        { text: 'May', value: '5' },
        { text: 'Jun', value: '6' },
        { text: 'Jul', value: '7' },
        { text: 'Aug', value: '8' },
        { text: 'Sep', value: '9' },
        { text: 'Oct', value: '10' },
        { text: 'Nov', value: '11' },
        { text: 'Dec', value: '12' },
      ],
      region: 'KR',
      regions: [
        { text: 'KR', value: 'KR' },
        { text: 'EU', value: 'EU' },
      ],
      AZ: 'KR',
      AZs: [
        { text: 'KR', value: 'KR' },
        { text: 'EU', value: 'EU' },
      ],
      tenant: 'KR',
      tenants: [
        { text: 'KR', value: 'KR' },
        { text: 'EU', value: 'EU' },
      ],
      status: 'KR',
      statuss: [
        { text: 'KR', value: 'KR' },
        { text: 'EU', value: 'EU' },
      ],
    }
  },
}
</script>

<style>
.select {
  display: inline-block;
  width: 120px;
  border: 1px solid #999;
  color: white;
}

.select .selected {
  display: flex;
  justify-content: space-between;
  padding: 8px 5px;
}

.select .selected .selected-value {
  max-width: 90px;
}

.select .selected .arrow {
  width: 24px;
  background: url('https://uxwing.com/wp-content/themes/uxwing/download/02-arrow-direction/arrow-bottom.png')
    no-repeat 70% 50%;
  background-size: 50% 50%;
}

.select ul {
  width: 120px;
  border: 1px solid #999;
  position: absolute;
  background: #fff;
  border-top: none;
  margin: 1px 0 0 -1px;
  cursor: pointer;
}

.select ul li {
  padding: 8px 5px;
}
</style>
