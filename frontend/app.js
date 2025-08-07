let idToken = null;
const apiURL = "https://joe-blog-pgif.onrender.com";

function handleCredentialResponse(response) {
  idToken = response.credential;
  document.getElementById("editor").style.display = "block";
  document.getElementById("signout").style.display = "inline-block";
  document.querySelector(".g_id_signin").style.display = "none";
  fetchPosts();
}

function signOut() {
  google.accounts.id.disableAutoSelect();
  idToken = null;
  document.getElementById("editor").style.display = "none";
  document.getElementById("signout").style.display = "none";
  document.querySelector(".g_id_signin").style.display = "block";
}

async function submitPost() {
  const title = document.getElementById("title").value.trim();
  const content = document.getElementById("content").value.trim();
  if (!title || !content || !idToken) {
    alert("Missing fields or not signed in");
    return;
  }

  const response = await fetch(`${apiURL}/posts/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, content, token: idToken })
  });
  console.log(JSON.stringify({ title, content, token: idToken }))
  if (response.ok) {
    alert("Post created!");
    document.getElementById("title").value = "";
    document.getElementById("content").value = "";
    fetchPosts();
  } else {
    alert("Error creating post");
  }
}

async function fetchPosts() {
  const res = await fetch(`${apiURL}/posts/`);
  const posts = await res.json();
  const list = document.getElementById("postList");
  list.innerHTML = "";

  posts.forEach(post => {
    const div = document.createElement("div");
    div.className = "post";
    div.innerHTML = `
      <h3>${post.title}</h3>
      <p class="date">By ${post.author} • ${new Date(post.created_at).toLocaleString()}</p>
      <p>${post.content.replace(/\n/g, "<br>")}</p>
    `;
    list.appendChild(div);
  });
}

// Fetch posts even for anonymous users
fetchPosts();
