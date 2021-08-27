import axios from "axios";

const BASE_URL = process.env.REACT_APP_BASE_URL || "http://localhost:5000";

/** FrienderApi Class.
 *
 * Static class tying together methods used to get/send to to the API.
 *
 */

class FrienderApi {
  currentUser = null;
  static async request(endpoint, data = {}, method = "get") {
    console.debug("API Call:", endpoint, data, method);
    const url = `${BASE_URL}/${endpoint}`;
    // const headers = { Authorization: `Bearer ${JoblyApi.token}` };
    const headers = { "Content-Type": "application/json" };
    const params = method === "get" ? data : {};

    try {
      console.log("HERE", url, method, data, headers, params);
      return (await axios({ url, method, data, params, headers })).data;
    } catch (err) {
      console.error("API Error:", err.response);
      let message = err.response.data.error.message;
      throw Array.isArray(message) ? message : [message];
    }
  }

  static async signup(signupData) {
    // Convert form data to snake case key's for the backend
    let data = {
      first_name: signupData.firstName,
      last_name: signupData.lastName,
      email: signupData.email,
      password: signupData.password,
      zipcode: signupData.zip,
      friend_radius: signupData.radius,
    };

    console.log("pre-stringified data: ", data);
    data = JSON.stringify(data);

    const res = await this.request("/signup", data, "post");
    console.log("API: signedup: response: ", res);
    // TODO: will refactor
    const user = {
      firstName: res.user.first_name,
      lastName: res.user.last_name,
      email: res.user.email,
      description: res.user.description,
      radius: res.user.friend_radius,
      zip: res.user.zipcode,
    };

    console.log("signedup user:", user);
    return user;
  }

  static async login(data) {
    console.log("logging in through API,", data.email, data.password);
    data = JSON.stringify(data);

    const res = await this.request("/login", data, "post");
    console.log("api, login: ", res);
    const {
      first_name,
      last_name,
      email,
      description,
      friend_radius,
      zipcode,
    } = res;
    const user = {
      firstName: first_name,
      lastName: last_name,
      email,
      description,
      radius: friend_radius,
      zip: zipcode,
    };
    return user;
  }

  // Individual API routes

  /** Get details on a company by handle. */

  // static async getCompany(handle) {
  //   let res = await this.request(`companies/${handle}`);
  //   return res.company;
  // }

  // /**Get and Filter a list of companies based off searchterm, */
  // static async filterCompanies(searchTerm) {
  //   let res;
  //   let data = { name: searchTerm };
  //   if (searchTerm === "") {
  //     res = await this.request(`companies`);
  //   } else {
  //     res = await this.request(`companies`, data);
  //   }
  //   return res.companies;
  // }

  // /**Get and Filter a list of jobs based off searchterm, */
  // static async filterJobs(searchTerm) {
  //   let res;
  //   let data = { title: searchTerm };
  //   if (searchTerm === "") {
  //     res = await this.request(`jobs`);
  //   } else {
  //     res = await this.request(`jobs`, data);
  //   }
  //   return res.jobs;
  // }

  // static async login(loginUserData) {
  //   const res = await this.request("auth/token", loginUserData, "post");

  //   console.log(res, " JOBLYAPI login")
  //   // console.log("ABOUT TO SET JOBLY API TOKEN")
  //   // this.token = res.token;
  //   return res.token;
  // }

  // static async getUserInfo(username) {
  //   const res = await this.request(`users/${username}`, username);

  //   // console.log(res, " JOBLYAPI getUser");
  //   return res.user;
  // }

  // //updates userinfo
  // static async updateProfile(profileInfo){
  //   const {username} =  jwt.decode(this.token)
  //   const res  =  await this.request(`users/${username}`, profileInfo, "patch")
  //   return res.user
  // }

  // static async apply(jobID){
  //   const {username} =  jwt.decode(this.token)
  //   const res  =  await this.request(`users/${username}/jobs/${jobID}`, {}, "post")
  //   return res
  // }

  // obviously, you'll add a lot here ...
}

// for now, put token ("testuser" / "password" on class)
// JoblyApi.token =
//   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZ" +
//   "SI6InRlc3R1c2VyIiwiaXNBZG1pbiI6ZmFsc2UsImlhdCI6MTU5ODE1OTI1OX0." +
//   "FtrMwBQwe6Ue-glIFgz_Nf8XxRT2YecFCiSpYL0fCXc";

export default FrienderApi;
