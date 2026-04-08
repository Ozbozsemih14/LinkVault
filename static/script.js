// 1. links fetch when page loads
document.addEventListener("DOMContentLoaded", () => {
    fetchLinks();
});

// 2. Fetch list function
async function fetchLinks() {
    try {
        const response = await fetch('/links');
        if (!response.ok) throw new Error('Backend cevap vermiyor');
        
        const links = await response.json();
        const listContainer = document.getElementById('linkList');

        listContainer.innerHTML = '';

        if (links.length === 0) {
            listContainer.innerHTML = '<p class="text-center text-gray-500">Henüz hiç link eklenmemiş</p>';
            return;
        }

        links.forEach(link => {
            
            listContainer.innerHTML += `
            <div class="bg-gray-800 p-4 rounded-xl flex justify-between items-center border border-gray-700 hover:border-blue-500 transition duration-300 shadow-md mb-3">
                <div class="flex flex-col text-left">
                    <h3 class="text-lg font-bold text-white">${link.title}</h3>
                    <a href="${link.url}" target="_blank" class="text-blue-400 text-sm hover:underline">${link.url}</a>
                </div>
                <button onclick="deleteLink(${link.id})" class="text-gray-500 hover:text-red-500 transition p-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                </button>
            </div>`;
        });
    } catch (error) {
        console.error("Linkler yüklenirken hata oluştu:", error);
    }
}

// 3. Link adding function
async function addLink() {
    const title = document.getElementById('titleInput').value;
    const url = document.getElementById('urlInput').value;

    if (!title.trim() ) {
        alert("Lütfen başlık giriniz!");
        return;
    } 
    if (!url.trim()){
        alert("Lütfen geçerli bir url giriniz!");
        return;
    } 
    if (!url.startsWith('http')) {
        alert("URL 'http' veya 'https' ile başlamalıdır! ");
        return;
    }

    const response = await fetch('/links', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, url })
    });

    if (response.ok) {
        document.getElementById('titleInput').value = '';
        document.getElementById('urlInput').value = '';
        fetchLinks(); // Listeyi tazele
    }
}

document.getElementById('urlInput').addEventListener('keypress',function(e){
    if (e.key ==='Enter'){
        addLink();
    }
});

// 4. Delete function
async function deleteLink(id) {
    if (confirm("Siliyorum, emin misin?")) {
        const response = await fetch(`/links/${id}`, { method: 'DELETE' });
        if (response.ok) fetchLinks();
    }
}