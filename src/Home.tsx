import './styles/Home.css'
import { saveStory } from './requests/requests'

function Home(){

    function saveStoryDefault(){
        saveStory(0, "Potatoes");
    }

    return (
        <>
        <div id = 'main-text-div'>
            <textarea id="main-text" name="main-text" rows="30" cols="100"/>
            <button onClick={saveStoryDefault}>Save</button>
        </div> 
        </>      
    );
}

export default Home