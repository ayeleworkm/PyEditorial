function showContent(tabName) {
    document.getElementById('content').innerText = {
        'mission': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Vitae voluptatum amet ad. Iusto consectetur magnam incidunt impedit voluptatum sequi possimus repellat ratione deserunt, adipisci corporis voluptates autem, quae ex eaque labore odio optio nam ut eveniet? Magni dignissimos fugit dolore excepturi nemo eligendi veniam aliquid error, animi incidunt? Nam, dolorum!',
        'vision': 'Vision is Lorem ipsum dolor sit amet consectetur adipisicing elit. Vitae voluptatum amet ad. Iusto consectetur magnam incidunt impedit voluptatum sequi possimus repellat ratione deserunt, adipisci corporis voluptates autem, quae ex eaque labore odio optio nam ut eveniet? Magni dignissimos fugit dolore excepturi nemo eligendi veniam aliquid error, animi incidunt? Nam, dolorum!',
        'objective': 'Our objective isLorem ipsum dolor sit amet consectetur adipisicing elit. Vitae voluptatum amet ad. Iusto consectetur magnam incidunt impedit voluptatum sequi possimus repellat ratione deserunt, adipisci corporis voluptates autem, quae ex eaque labore odio optio nam ut eveniet? Magni dignissimos fugit dolore excepturi nemo eligendi veniam aliquid error, animi incidunt? Nam, dolorum!'
    }[tabName];
    
    document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
    document.getElementById(tabName).classList.add('active');
}
