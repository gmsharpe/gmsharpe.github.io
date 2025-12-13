import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

// ------------------------------------------------------------------
// This simple component renders the "Hero" banner at the top
// ------------------------------------------------------------------
function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--dark')} style={{backgroundColor: '#1b1b1d', color: 'white'}}>
      <div className="container">
        <div className="row">
          <div className="col col--6" style={{display: 'flex', flexDirection: 'column', justifyContent: 'center'}}>
            <h1 className="hero__title">{siteConfig.title}</h1>
            <p className="hero__subtitle">{siteConfig.tagline}</p>
            <div className={styles.buttons} style={{marginTop: '20px'}}>
              <Link
                className="button button--primary button--lg"
                to="/blog">
                Read My Articles
              </Link>
            </div>
          </div>
          <div className="col col--6" style={{textAlign: 'center'}}>
            {/* If you want your face here, uncomment below */}
            {/* <img src="/img/bio_portrait.webp" style={{borderRadius: '50%', maxWidth: '250px', border: '4px solid #25c2a0'}} /> */}
          </div>
        </div>
      </div>
    </header>
  );
}

// ------------------------------------------------------------------
// This is the main Layout of the home page
// ------------------------------------------------------------------
export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Backend Engineering, Data Analytics, and Swing Dancing">
      
      <HomepageHeader />
      
      <main style={{padding: '2rem', maxWidth: '800px', margin: '0 auto'}}>
        <section>
          <h2>Welcome</h2>
          <p>
            This is my digital garden for technical documentation, cloud architecture notes, 
            and data analytics projects. I've worked for over 10 years building backend 
            systems at enterprise scale.
          </p>
          <p>
            Feel free to explore my <strong>Technical Articles</strong> for tutorials on 
            Python, Cloud Infrastructure, and Data Engineering, or check out the 
            <strong>About</strong> page to learn more about my background in Sociology 
            and Swing Dancing.
          </p>
          
          <h3>Recent Topics</h3>
          <ul>
            <li>Cloud Solutions Architecture</li>
            <li>Data Synchronization & Munging</li>
            <li>Backend Engineering Patterns</li>
          </ul>
        </section>
      </main>
    </Layout>
  );
}