import React from 'react';

export function Reference({ number, author, title, url, publication, year }) {
  return (
    <div style={{ 
      marginLeft: '20px', 
      marginBottom: '10px', 
      fontSize: '0.9em',
      lineHeight: '1.5'
    }}>
      {number && <strong>[{number}] </strong>}
      {author && <span>{author}, </span>}
      {title && <em>"{title},"</em>}
      {publication && ` ${publication},`}
      {year && ` ${year}.`}
      {url && (
        <> [Online]. Available: <a href={url} target="_blank" rel="noopener noreferrer">{url}</a></>
      )}
    </div>
  );
}

export function References({ children }) {
  return (
    <div style={{ 
      marginTop: '2rem', 
      paddingTop: '1rem', 
      borderTop: '2px solid var(--ifm-color-emphasis-300)' 
    }}>
      <h2>References</h2>
      {children}
    </div>
  );
}
