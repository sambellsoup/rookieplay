var x = 0
var y = 1
var a, z = "";

var job_type = []
var cursor = []
var city = []
var salary_offered = []
var url = []
var job_description = []
var job_board = []
var post_date = []
var company_name = []
var category = []
var job_title = []

console.log("THIS IS STATIC")
console.log("x-value: ", x)

// console.log({{ client_auth_key_value | safe }})


// client_id_value = 'rooki_jp_sandbox_e7fea44cf2'
// client_auth_key_value = 't2PM7wVV5Ij2wyJ-caRNuQEB6JsFImTjitzX60UElyY'


/*
$(function (){

  $.ajax({

  });

});

*/

function thumbsup(key){
  if (x === 10){
    document.getElementById("demo" + x).innerHTML = "Please close a job search box."

  }
  else{
    console.log("x-value after thumbs up: ", x)
    thumbs_up_list.push(jobs[key]);
    // Use job title to conduct google search for links to live job ads
    var q = jobs[key]
    // window.open('https://serpapi.com/search.json?engine=google_jobs&q=' + q + '+new+york&hl=en')
    document.getElementById("demoa" + x).innerHTML = q


    x++
        console.log("x-value after thumbs up and add: ", x)

    // Replace old job title with a new job title to receive judgment from user
    jobs[key] = jobs_bank[0]
    document.getElementById("menu" + key).innerHTML = jobs_bank[0]
    jobs_bank.splice(0, 1)


    var request = new XMLHttpRequest();

    request.open('POST', 'https://api.jobspikr.com/v2/data');

    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('client_id', client_id_value);
    request.setRequestHeader('client_auth_key', client_auth_key_value);

    request.onreadystatechange = function () {
      if (this.readyState === 4) {
        console.log('Status:', this.status);
        console.log('Headers:', this.getAllResponseHeaders());
        console.log('Body:', this.responseText);
      }
    };

    var body = {
      'size': 50,
      'cursor': 1549411216369936,
      'format': 'json',
      'search_query_json': {
        'query_string': {
          'default_field': 'job_title',
          'query': 'marketing'
        }
      }
    };

    request.send(JSON.stringify(body));


        // console.log("The cursor is", body.cursor)
        // console.log("this is myObj", myObj);

/*
        for (a in myObj.job_data) {
	         z += "Job Type: " + myObj.job_data[a].job_type + " "
           z += "Cursor: " + myObj.job_data[a].cursor + " "
           z += "City: " + myObj.job_data[a].city + " "
	         z += "Salary Offered: " + myObj.job_data[a].salary_offered + " "
	         z += "URL: " + myObj.job_data[a].url + " "
	         z += "Job Description: " + myObj.job_data[a].job_description + " "
 	         z += "Job Board: " + myObj.job_data[a].job_board + " "
 	         z += "Post Date: " + myObj.job_data[a].post_date + " "
	         z += "Company Name: " + myObj.job_data[a].company_name + " "
	         z += "Category: " + myObj.job_data[a].category + " "
	         z += "Job Title: " + myObj.job_data[a].job_title + " "
           console.log(z)

           job_type.push(myObj.job_data[a].job_type)
           cursor.push(myObj.job_data[a].cursor)
           city.push(myObj.job_data[a].city)
	         salary_offered.push(myObj.job_data[a].salary_offered)
	         url.push(myObj.job_data[a].url)
	         job_description.push(myObj.job_data[a].job_description)
 	         job_board.push(myObj.job_data[a].job_board)
 	         post_date.push(myObj.job_data[a].post_date)
	         company_name.push(myObj.job_data[a].company_name)
	         category.push(myObj.job_data[a].category)
	         job_title.push(myObj.job_data[a].job_title)
         }
*/

    $(function (){

        $(".btn").click(function(){
          $.ajax({
            url: '',
            type: 'get',
            data: {
              button_text: q
            },
            success: function(response) {
              $(".btn").text(response.seconds)
              $("#seconds").append('<li>' + response.seconds + '</li>')
            }
          });
        });

      });
    }

}
