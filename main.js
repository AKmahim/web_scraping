const axios = require('axios');
const cheerio = require('cheerio');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

// Send a GET request to the main page with the list of links
const mainUrl = 'https://github.com/ethereum/EIPs/tree/master/EIPS';

axios.get(mainUrl)
  .then((response) => {
    const baseurl = 'https://github.com';
    const wrongLinkList = [
      "https://github.com",
      "/ethereum/EIPs/tree/597592eeb9cca9221a27fcff8fb7b64b7d0834a5/EIPS",
    "https://docs.github.com/site-policy/github-terms/github-terms-of-service",
    "https://docs.github.com/site-policy/privacy-policies/github-privacy-statement",
    "https://github.com/security","https://www.githubstatus.com/",
    "https://docs.github.com",
    "https://support.github.com?tags=dotcom-footer",
    "https://github.com/pricing",
    "https://docs.github.com",
    "https://services.github.com",
    "https://github.blog",
    "https://github.com/about",
    "#start-of-content",
    "https://github.com/",
    "/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&source=header-repo",
    "/features/actions",
    "/features/packages",
    "/features/security",
    "/features/codespaces",
    "/features/copilot",
    "/features/code-review",
    "/features/issues",
    "/features/discussions",
    "/features",
    "https://skills.github.com/",
    "/enterprise",
    "/team",
    "/enterprise/startups",
    "https://education.github.com",
    "/solutions/ci-cd/",
    "https://resources.github.com/devops/",
    "https://resources.github.com/devops/fundamentals/devsecops/",
    "/customer-stories",
    "https://resources.github.com/",
    "/sponsors",
    "/readme",
    "/topics",
    "/trending",
    "/collections",
    "/pricing",
    "/login?return_to=https%3A%2F%2Fgithub.com%2Fethereum%2FEIPs%2Ftree%2Fmaster%2FEIPS",
    "/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&source=header-repo&source_repo=ethereum%2FEIPs",
    "/ethereum",
    "/ethereum/EIPs",
    "/login?return_to=%2Fethereum%2FEIPs",
    "/login?return_to=%2Fethereum%2FEIPs",
    "/login?return_to=%2Fethereum%2FEIPs",
    "/ethereum/EIPs",
    "/ethereum/EIPs/issues",
    "/ethereum/EIPs/pulls",
    "/ethereum/EIPs/actions",
    "/ethereum/EIPs/security",
    "/ethereum/EIPs/pulse",
    "/ethereum/EIPs",
    "/ethereum/EIPs/issues",
    "/ethereum/EIPs/pulls",
    "/ethereum/EIPs/actions",
    "/ethereum/EIPs/security",
    "/ethereum/EIPs/pulse",
    "https://github.com/ethereum/EIPs/tree/{{ urlEncodedRefName }}/EIPS",
    "/ethereum/EIPs/branches",
    "https://github.com/ethereum/EIPs/tree/{{ urlEncodedRefName }}/EIPS",
    "/ethereum/EIPs/tags",
    "/ethereum/EIPs",
    "/ethereum/EIPs/find/master",
    "/ethereum/EIPs",
    "/ethereum/EIPs/commits/master/EIPS",
    "/ethereum/EIPs/tree/2fd73316d4282fe3f379319da812f27c8f7f5cf0/EIPS",
    "/ethereum/EIPs/tree/df55bdd3b592e0f08d7197ace05c56cee4d574b6/EIPS"
      // ... list of unwanted links
    ];

    // Create a Cheerio instance from the main page HTML content
    const $ = cheerio.load(response.data);

    // Find the list of links on the main page
    const links = $('a');

    // Create a CSV writer
    const csvWriter = createCsvWriter({
      path: 'data_from_js.csv',
      header: [] // add column headers if required
    });

    const data = [];

    // Iterate over each link and extract table data from the linked page
    links.each((index, element) => {
      const linkedUrl = $(element).attr('href');
      if (wrongLinkList.includes(linkedUrl)) {
        return;
      }

      const fullUrl = baseurl + linkedUrl;

      // Send a GET request to the linked page
      axios.get(fullUrl)
        .then((linkedResponse) => {
          // Create a Cheerio instance from the linked page HTML content
          const linked$ = cheerio.load(linkedResponse.data);

          // Extract data from the table on the linked page
          const table = linked$('table');

          if (table.length > 0) {
            const rows = table.find('tr');

            // Extract the table data and add it to the data array
            rows.each((rowIndex, rowElement) => {
              const rowData = [];
              const columns = cheerio(rowElement).find('td');

              columns.each((columnIndex, columnElement) => {
                rowData.push(cheerio(columnElement).text());
              });

              data.push(rowData);
            });
          } else {
            console.log('No table found on the linked page:', fullUrl);
          }

          // Write table data to the CSV file
          csvWriter.writeRecords(data)
            .then(() => {
              console.log('Table data has been written to data.csv');
            })
            .catch((error) => {
              console.error('Failed to write table data:', error);
            });
        })
        .catch((error) => {
          console.error('Failed to fetch linked page:', error);
        });
    });
  })
  .catch((error) => {
    console.error('Failed to fetch main page:', error);
  });
