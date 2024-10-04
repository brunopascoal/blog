// Toggle sidebar
document.getElementById('sidebarCollapse').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('active');
});

// Dark mode toggle
document.getElementById('darkModeToggle').addEventListener('change', function() {
    document.body.classList.toggle('dark-mode');
});

// Dynamically add blog posts
const blogPosts = [
    { title: 'First Blog Post', excerpt: 'This is a short excerpt of the first blog post...', image: 'https://picsum.photos/300/200?random=1' },
    { title: 'Second Blog Post', excerpt: 'This is a short excerpt of the second blog post...', image: 'https://picsum.photos/300/200?random=2' },
    { title: 'Third Blog Post', excerpt: 'This is a short excerpt of the third blog post...', image: 'https://picsum.photos/300/200?random=3' },
    { title: 'Fourth Blog Post', excerpt: 'This is a short excerpt of the fourth blog post...', image: 'https://picsum.photos/300/200?random=4' },
    { title: 'Fifth Blog Post', excerpt: 'This is a short excerpt of the fifth blog post...', image: 'https://picsum.photos/300/200?random=5' },
    { title: 'Sixth Blog Post', excerpt: 'This is a short excerpt of the sixth blog post...', image: 'https://picsum.photos/300/200?random=6' }
];

const blogPostsContainer = document.getElementById('blogPosts');
blogPosts.forEach(post => {
    const postElement = document.createElement('div');
    postElement.className = 'col-md-4 mb-4';
    postElement.innerHTML = `
        <div class="card h-100">
            <img src="${post.image}" class="card-img-top" alt="${post.title}">
            <div class="card-body">
                <h5 class="card-title">${post.title}</h5>
                <p class="card-text">${post.excerpt}</p>
                <a href="#" class="btn btn-primary">Read more</a>
            </div>
        </div>
    `;
    blogPostsContainer.appendChild(postElement);
});
