// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const {themes} = require('prism-react-renderer');
const lightCodeTheme = themes.github;
const darkCodeTheme = themes.dracula;

/** @type {import('@docusaurus/types').Config} */
const config = {
  // -------------------------------------------------------------------------
  // 1. GITHUB PAGES DEPLOYMENT SETTINGS (CRITICAL)
  // -------------------------------------------------------------------------
  title: 'Your Name',                // REPLACE WITH YOUR NAME
  tagline: 'Backend Engineer & Cloud Solutions Architect',
  
  url: 'https://gmsharpe.github.io'
  baseUrl: '/',
  
  organizationName: 'gmsharpe',      
  projectName: 'gmsharpe.github.io',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',

  // -------------------------------------------------------------------------
  // 2. PRESETS & CONTENT CONFIG
  // -------------------------------------------------------------------------
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // This allows people to click "Edit this page" and go to your repo
          editUrl: 'https://github.com/gmsharpe/gmsharpe/tree/main/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/gmsharpe/gmsharpe/tree/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  // -------------------------------------------------------------------------
  // 3. THEME & NAVIGATION
  // -------------------------------------------------------------------------
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Your Name', // Appears in top left
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg', // You can replace this file in static/img/ later
        },
        items: [
          // --- NAVIGATION LINKS ---
          {
            to: '/about',     // Links to src/pages/about.md
            label: 'About',
            position: 'left',
          },
          // --- SOCIAL LINKS ---
          {
            href: 'https://github.com/gmsharpe', // REPLACE
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Content',
            items: [
              {
                label: 'About Me',
                to: '/about',
              },
            ],
          },
          {
            title: 'Connect',
            items: [
              {
                label: 'Medium',
                href: 'https://medium.com/@gmsharpe', // REPLACE
              },
              {
                label: 'LinkedIn',
                href: 'https://linkedin.com/in/gmsharpe', // REPLACE
              },
              {
                label: 'GitHub',
                href: 'https://github.com/gmsharpe', // REPLACE
              },
            ],
          },
        ],
        // --- LICENSE DECLARATION ---
        copyright: `Copyright © ${new Date().getFullYear()} Your Name. <br/> 
        Except where otherwise noted, content is CC BY 4.0; Code is MIT.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
        // Added 'hcl' (Terraform) and 'python' support explicitly
        additionalLanguages: ['hcl', 'python', 'bash', 'json'], 
      },
    }),
};

module.exports = config;
