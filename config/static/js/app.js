    const { algoliasearch, instantsearch } = window;

    const searchClient = algoliasearch('OBK7X8M1VB', '6c0b093354161d05692796dcfc71a77c');

    const search = instantsearch({
        indexName: 'indice_personas',
        searchClient,
    });

    search.addWidgets([
        instantsearch.widgets.searchBox({
            container: '#searchbox',
        }),
        instantsearch.widgets.hits({
            container: '#hits',
            templates: {
            item: `
        <article>
        <strong>{{#helpers.highlight}}{ "attribute": "firstname" }{{/helpers.highlight}}</strong>
        <p>{{#helpers.highlight}}{ "attribute": "lastname" }{{/helpers.highlight}}</p>
        </article>
        `,
            },
        }),
        instantsearch.widgets.configure({
            hitsPerPage: 8,
        })
    ]);

    search.start();
