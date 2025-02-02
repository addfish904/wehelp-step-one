document.addEventListener("DOMContentLoaded", function () {
    const apiUrl = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";
    let currentIndex = 3; // 初始索引，前三個用於 small-boxes
    const initialLoad = 10; // 初始載入 10 個
    const itemsPerLoad = 10; // 每次按下按鈕再加載 10 個

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const spots = data.data.results;
            const smallBoxes = document.querySelectorAll(".small-box");
            const bigBoxesContainer = document.querySelector(".big-boxes");
            
            // 初始化 small-boxes
            for (let i = 0; i < 3; i++) {
                const img = smallBoxes[i].querySelector("img");
                const title = smallBoxes[i].querySelector("p");

                let imgUrl = spots[i].filelist.split("https://")[1];
                img.src = "https://" + imgUrl;
                img.alt = spots[i].stitle;
                title.textContent = spots[i].stitle;
            }
            
            function renderMoreBigBoxes(count) {
                let fragment = document.createDocumentFragment();
                for (let i = currentIndex; i < currentIndex + count && i < spots.length; i++) {
                    const box = document.createElement("div");
                    box.classList.add("box");
                    if ((i - currentIndex) % 5 === 0) {
                        box.classList.add("first-column");
                    }
                    
                    const icon = document.createElement("i");
                    icon.classList.add("fa-solid", "fa-star");
                    icon.style.color = "#FFD43B";
                    
                    const titleDiv = document.createElement("div");
                    titleDiv.classList.add("box-title");
                    const titleP = document.createElement("p");
                    titleP.textContent = spots[i].stitle;
                    titleDiv.appendChild(titleP);
                    
                    box.appendChild(icon);
                    box.appendChild(titleDiv);
                    
                    let imgUrl = spots[i].filelist.split("https://")[1];
                    box.style.backgroundImage = `url('https://${imgUrl}')`;
                    
                    fragment.appendChild(box);
                }
                bigBoxesContainer.appendChild(fragment);
                currentIndex += count;
            }
            
            renderMoreBigBoxes(initialLoad);
            
            const loadMoreButton = document.getElementById("loadMore");
            loadMoreButton.addEventListener("click", function () {
                if (currentIndex < spots.length) {
                    renderMoreBigBoxes(itemsPerLoad);
                }
                if (currentIndex >= spots.length) {
                    loadMoreButton.style.display = "none"; // 資料顯示完後隱藏按鈕
                }
            });
        });
});
