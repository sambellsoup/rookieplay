var x = 0
var y = 1
var a, z = "";

var job_type = []
var cursor = []
var city = []
var state = []
var salary_offered = []
var url = []
var job_description = []
var job_board = []
var post_date = []
var company_name = []
var category = []
var job_title = []
var thumbs_up_list = []




function thumbsup(key){
  if (x === 10){
    document.getElementById("demo" + x).innerHTML = "Please close a job search box."

  }
  else{
    thumbs_up_list.push(jobs[key]);
    console.log('test')
    console.log('thumbs up list: ' + thumbs_up_list)
    // Use job title to conduct google search for links to live job ads
    var q = jobs[key]

    // window.open('https://serpapi.com/search.json?engine=google_jobs&q=' + q + '+new+york&hl=en')
    // document.getElementById("demoa" + x).innerHTML = q

    // Replace old job title with a new job title to receive judgment from user
    jobs[key] = jobs_bank[0]
    document.getElementById("menu" + key).innerHTML = jobs_bank[0]

    // Removes job from list
    jobs_bank.splice(0, 1)




    var request = new XMLHttpRequest();

    request.open('POST', 'https://api.jobspikr.com/v2/data');

    request.setRequestHeader('Content-Type', 'application/json');

    request.onreadystatechange = function () {
      if (this.readyState === 4) {
        console.log("Job Query: " + q)

        var myObj = JSON.parse(this.responseText);
        for (a in myObj.job_data){
          job_type.push(myObj.job_data[a].job_type)
          cursor.push(myObj.job_data[a].cursor)
          city.push(myObj.job_data[a].city)
          state.push(myObj.job_data[a].state)
          salary_offered.push(myObj.job_data[a].salary_offered)
          url.push(myObj.job_data[a].url)
          job_description.push(myObj.job_data[a].job_description)
          job_board.push(myObj.job_data[a].job_board)
          post_date.push(myObj.job_data[a].post_date)
          company_name.push(myObj.job_data[a].company_name)
          category.push(myObj.job_data[a].category)
          job_title.push(myObj.job_data[a].job_title)
          document.getElementById("demoa" + x).innerHTML = q
          document.getElementById("demob" + x).innerHTML = "Job Title: " + job_title[x];
          document.getElementById("democ" + x).innerHTML = "Location: " + city[x] + "," + state[x];
          document.getElementById("demod" + x).innerHTML = "Posted: " + post_date[x];
          document.getElementById("demoe" + x).innerHTML = "Apply Here".link(url[x]);
          document.getElementById("demof" + x).innerHTML = "Company Name: " + company_name[x];
          document.getElementById("demog" + x).innerHTML = "Job Description: " + job_description[x];
          x++
        }

        console.log('These are the recommended job titles: ' + job_title)


      }
    };
      };
    }

    $(".thumb-up").click(function(){
      console.log("This is a test for the job title inside the ajax function.", q)
      var job_title;
      job_title = q
          $.ajax({
            url: '',
            type: 'GET',
            data: {
              button_text: q
            },
            success: function(response) {
              $(".btn").text(response.seconds)
              $("#seconds").append('<li>' + response.seconds + '</li>')
            }
          });
        });
