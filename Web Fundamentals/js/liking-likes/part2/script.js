function like(e) {
    var likeCount = Number(e.parentElement.querySelector("#like-count").textContent);
    likeCount += 1;
    e.parentElement.querySelector("#like-count").textContent = likeCount;
}