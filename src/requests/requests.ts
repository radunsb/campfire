import axios from "axios";

export async function saveStory(userID: number, storyContents: string){
    const url = `${__BACKEND_URL__}/api/v1/stories/new/${userID}`
    const data = {"user_id": userID, "contents": storyContents};
    await axios.post(url,{
            data:data,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
    return 0;
}