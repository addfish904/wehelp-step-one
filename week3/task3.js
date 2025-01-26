document.addEventListener("DOMContentLoaded", function () {
    const apiUrl = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";

    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      const spots = data.data.results; 
      const smallBoxes = document.querySelectorAll(".small-box");
      const bigBoxes = document.querySelectorAll(".box");
      const loadMoreButton = document.getElementById("loadMore");

      for (let i = 0; i < 3; i++) {
        const img = smallBoxes[i].querySelector("img");
        const title = smallBoxes[i].querySelector("p");

        let imgUrl = "";
        if (spots[i].filelist) {
          let parts = spots[i].filelist.split("https://");
          if (parts.length > 1) {
            imgUrl = "https://" + parts[1];
          }
        }
        img.src = imgUrl;
        img.alt = spots[i].stitle;
        title.textContent = spots[i].stitle;
      }

      const startIndex = 3; 
      for (let i = 0; i < 10; i++) {
        const bigBox = bigBoxes[i];
        const imgUrl = spots[startIndex + i].filelist.split("https://")[1];
        const title = bigBox.querySelector(".box-title p");

        bigBox.style.backgroundImage = `url('https://${imgUrl}')`;
        title.textContent = spots[startIndex + i].stitle;
      }
    })
    .catch(error => console.error("Error fetching data:", error));
});
