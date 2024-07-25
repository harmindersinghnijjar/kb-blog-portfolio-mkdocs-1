---
title: Harminder's Knowledge Base
authors: [harmindersinghnijjar]
nav_order: 1
description: Dive into Harminder's Knowledge Base, where I share insights, tutorials, and projects on a wide range of tech topics.
keywords: tech tutorials, machine learning, web development, object detection, knowledge base
tags: [machine learning, web development, object detection, knowledge base]
hide:
  - navigation
  - toc
  - feedback
permalink: /
---

<!DOCTYPE html>
<html lang="en">
<head>

  <!-- Google icons -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

  <!-- Tailwind CSS -->
  <link href="https://unpkg.com/tailwindcss@latest/dist/tailwind.min.css" rel="stylesheet">

  <!-- Favicon -->
  <link rel="shortcut icon" href="https://www.mkdocs.org/favicon.ico" type="image/x-icon">

  <!-- ApexCharts library -->
  <script src="https://cdn.jsdelivr.net/npm/apexcharts@latest/dist/apexcharts.min.js"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Custom styles -->
  <link rel="stylesheet" href="css/custom.css">

  <meta name="viewport" content="width=device-width, initial-scale=1.0">


</head>

<body>
  <div class="flex flex-wrap -mx-4">
    <!-- Left Column: Large Card on the Top, Third Card on the Bottom -->
    <div class="w-full lg:w-2/3 px-4">
      <!-- Card 1: Large Card -->
      <div class="mb-4 p-8 rounded-lg shadow-2xl hover:shadow-xl hover:-translate-y-1 transform transition bg-teal-100 text-center">
        <h1 class="text-2xl font-bold mb-4 text-teal-900 hover:text-teal-600">Harminder's Knowledge Base</h1>
        <p class="text-teal-700 mb-4">
          A repository of personal knowledge that I update from time to time when I find interesting information, code or go down a rabbit hole of learning.

        </p>
        <p class="text-teal-700 mb-4">
          <!-- Some other areas of interest of mine include: intelligent single and multi-agent systems, cognitive frameworks, and productivity. -->
          I'm currently looking into assest and inventory management systems, and how they can be improved using machine learning, autonmous ground vehicles and drones, home automation and CAD design for 3D printing.
        </p>
        <p class="text-teal-700 mb-4">
          I also blog about my experiences and learnings on a nearly daily basis as I find it to be a creative outlet, a way of documenting my journey and a way to stay motivated and accountable.
        </p>
        <div class="mt-6">
          <a href="https://www.linkedin.com/in/harmindersinghnijjar/" target="_blank" rel="noopener noreferrer" class="text-teal-500 hover:text-teal-600 hover:underline">You can reach out to me on LinkedIn.</a>
        </div>
      </div>

      <!-- Card 3: Additional Content -->
      <div class="mb-4 p-8 rounded-lg shadow-2xl hover:shadow-xl hover:-translate-y-1 transform transition bg-teal-100 text-center">
        <h2 class="text-xl font-bold mb-4 text-teal-900">GitHub Activity</h2>
        <div class="github-heatmap">
        <img src="https://ghchart.rshah.org/harmindersinghnijjar" alt="Harminder's GitHub Contributions">
      </div>

      </div>
    </div>

    <!-- Right Column: OSRS Weekly Stats Gained Card -->
    <div class="w-full lg:w-1/3 px-4">
      <div id="osrs-weekly-stats-gained-card" class="p-1 rounded-lg shadow-2xl hover:shadow-xl hover:-translate-y-1 transform transition bg-teal-100 text-center h-full">
        <h2 class="text-xl font-bold mb-4 text-teal-900">OSRS Tracker</h2>
        <div id="osrs-weekly-stats-gained-container" class="p-0">
          <!-- Weekly stats gained will be populated here by JavaScript -->
        </div>
      </div>
    </div>

  </div> <!-- End of .flex .flex-wrap -->
  
  <script type="module">
  // This function will fetch OSRS player weekly gains and update the HTML content
  async function fetchAndDisplayOSRSWeeklyGains(playerName) {
    try {
      // Fetch the player gains using the Wise Old Man API
      const response = await fetch(`https://api.wiseoldman.net/v2/players/${encodeURIComponent(playerName)}/gained?period=week`, {
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (!response.ok) {
        throw new Error('Player gains could not be retrieved');
      }

      const playerGains = await response.json();

      // Select the container where the gains will be displayed
      const gainsContainer = document.getElementById('osrs-weekly-stats-gained-container');

      // Clear any existing content in the gains container
      gainsContainer.innerHTML = '';

      // Create a table to hold the skill rows
      const table = document.createElement('table');
      table.className = 'w-full min-w-full';
      
      // Create and append the header row
      const headerRow = document.createElement('tr');
      headerRow.className = "border-b border-gray-600";
      headerRow.innerHTML = `
        <th class="whitespace-nowrap p-4 align-middle">Skill</th>
        <th class="whitespace-nowrap p-4 align-middle">XP Gained</th>
        <th class="whitespace-nowrap p-4 align-middle">Levels Gained</th>
      `;
      table.appendChild(headerRow);

      // Sort skills by experience gained
      const sortedSkills = Object.entries(playerGains.data.skills).sort((a, b) => b[1].experience.gained - a[1].experience.gained);

      // Take only the top 5 skills
      const topSkills = sortedSkills.slice(0, 5);

      // Loop through the top 5 skills and create table rows for each one
      topSkills.forEach(([skill, data], index) => {
        const row = document.createElement('tr');
        row.className = `border-b border-gray-600 ${index % 2 === 0 ? 'bg-gray-500' : 'bg-teal-200'} hover:bg-gray-600 transition-colors relative cursor-pointer`;

        // Skill icon and name always shown
        const skillCell = document.createElement('td');
        skillCell.className = "whitespace-nowrap p-4 align-middle";
        skillCell.innerHTML = `<div class="flex items-center gap-x-2"> <img alt="${skill}" loading="lazy" width="16" height="16" decoding="async" class="shrink-0" src="https://raw.githubusercontent.com/wise-old-man/wise-old-man/4c9374bed80cf6eb622b4bddb38f29fb764462ed/app/public/img/metrics/${skill}.png"> ${skill.charAt(0).toUpperCase() + skill.slice(1)} </div>`;

        // XP gained - always shown
        const xpCell = document.createElement('td');
        xpCell.className = "whitespace-nowrap p-4 align-middle";
        xpCell.innerHTML = `<span>${data.experience.gained.toLocaleString()}</span>`;

        // Level gained - always showm
        const levelCell = document.createElement('td');
        levelCell.className = "whitespace-nowrap p-4 align-middle";
        levelCell.innerHTML = `<span>${data.level.gained.toLocaleString()}</span>`;

        // Append the cells to the row
        row.appendChild(skillCell);
        row.appendChild(xpCell);
        row.appendChild(levelCell);

        // Append the row to the table
        table.appendChild(row);
      });

      // Append the table to the gainsContainer
      gainsContainer.appendChild(table);

      // Call the adjustFontSize function here, after the table is in the DOM
      adjustFontSize();
    } catch (error) {
      console.error('Error fetching OSRS weekly gains:', error);
      const gainsContainer = document.getElementById('osrs-weekly-stats-gained-container');
      gainsContainer.innerHTML = '<p>Error fetching weekly gains. Please try again later.</p>';
    }
  }

  // Replace 'yourPlayerName' with the actual player name
  fetchAndDisplayOSRSWeeklyGains('smfddumbho');

  // Add an image on the bottom of the card with the remaining height to fill the card
  const osrsWeeklyStatsGainedCard = document.getElementById('osrs-weekly-stats-gained-card');
  const osrsWeeklyStatsGainedCardImage = document.createElement('img');
  osrsWeeklyStatsGainedCardImage.src = 'github.png';

  // Add the image to the card if there is extra space (typically on larger screens)
  if (osrsWeeklyStatsGainedCard.offsetHeight > 400) {
    osrsWeeklyStatsGainedCard.appendChild(osrsWeeklyStatsGainedCardImage);
  }

  // This function will adjust the font size of the table based on the container width
  function adjustFontSize() {
    const osrsWeeklyStatsGainedContainer = document.getElementById('osrs-weekly-stats-gained-container');
    const osrsWeeklyStatsGainedTable = osrsWeeklyStatsGainedContainer.querySelector('table');

    // Ensure the table is present before attempting to adjust font size
    if (osrsWeeklyStatsGainedTable) {
    const containerWidth = osrsWeeklyStatsGainedContainer.offsetWidth;
    let fontSize = 16; // Default font size for desktop

        // Check if on mobile
        if (window.matchMedia("(max-width: 600px)").matches) {
          // If on mobile, scale down the font size
          fontSize = 12;
        } else {
          // For larger screens, adjust font size based on container width
          fontSize = Math.min(16, Math.max(12, Math.floor(containerWidth / 100)));
        }

        osrsWeeklyStatsGainedTable.style.fontSize = `${fontSize}px`;

}
}


  // Add an event listener to call adjustFontSize when the window resizes
  window.addEventListener('resize', adjustFontSize);
</script>
</body>
</html>
