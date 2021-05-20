<template>
<div>
  <div class="hello">
   <div>
    
  
    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold text-gray-900">
          Students
        </h1>
      </div>
    </header>
    <main>
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <!-- Replace with your content -->
        <div class="px-4 py-6 sm:px-0">
          <div class="flex flex-col">
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
        <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-green-100">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Student Name
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Gender
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Age
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Paid Fees?
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <span class="sr-only">Edit</span>
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Edit/Delete
                </th>
                
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
         
          <!-- looping through the students array object -->

              <tr v-for="(student, index) in students" :key="index">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 h-10 w-10">
                      <img class="h-8 w-8 rounded-full" src="../assets/girl.jpg" alt="">
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900">
                        {{ student.firstname }}
                      </div>
                      <div class="text-sm text-gray-500">
                        {{ student.lastname }}
                      </div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">{{ student.gender }}</div>
                  <!-- <div class="text-sm text-gray-500">Optimization</div> -->
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ student.age }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                    <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800" v-if="student.paid">Yes</span>
                    <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-green-800" v-else>No</span>
                  
                </td>
                
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <a href="#" class="text-indigo-600 hover:text-indigo-900"  @click="editStudent(student)">Edit</a>
                </td>
               <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <a href="#" class="text-indigo-600 hover:text-indigo-900"   @click="onDeleteStudent(student)">Delete</a>
                </td>
              </tr>
  
              <!-- More people... -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

        </div>
        <!-- /End replace -->
      </div>
    </main>
  </div>
  </div>
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "Students",
  
   data() {
    return {
      students: [],

      message: '',
      showMessage: false,

      addStudentForm: {
        firstname: '',
        lastname: '',
        gender: '',
        age: '',
        paid: [],
      },
      
      editForm: {
        id: '',
        firstname: '',
        lastname: '',
        gender: '',
        age: '',
        paid: [],
      },
      // exampleModalShowing: false,
    };
  },
  methods: {
    getStudents() {
      const path = 'http://localhost:5000/students';
      axios.get(path)
        .then((res) => {
          this.students = res.data.students;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  
},
created() {
    this.getStudents();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

a {
  color: #42b983;
}
</style>
