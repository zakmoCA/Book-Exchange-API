

function Home() {


  return (
    <>
      <div className="home-container">
        <nav>
          <ul>
            <li>Home</li>
            <li>My Library</li>
            <li>Sign In</li>
            <li>Join</li>
          </ul>
        </nav>
        <div className="collections-container">
          <p>Collections in your area</p>
          <div className="collections-carousel">
            <article>a</article>
            <article>b</article>
            <article>c</article>
            <article>d</article>
          </div>
        </div>
        <div className="search-container">
          <input type="text" placeholder="Search for a book..." />
        </div>
        <footer>
          <p>About app</p>
        </footer>
      </div>
    </>
  )
}

export default Home