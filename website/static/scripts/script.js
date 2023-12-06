newPostButton = document.querySelector('.createPostbtn');
postBox = document.querySelector('.createPost');

newPostButton.addEventlistener('click', makeNewPost);

function makeNewPost(){
    postBox.classList.remove('hidden');
    newPostButton.classList.add('hidden');
}