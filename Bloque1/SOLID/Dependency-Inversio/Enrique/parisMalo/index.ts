class Paris2024Provider{
    top(n: number){
        const data = [
            {rank: 1, country: "usa", gold: 40, silver: 44, bronze: 42},
            {rank: 2, country: "chn", gold: 40, silver: 27, bronze: 24},
            {rank: 3, country: "jpn", gold: 25, silver: 23, bronze: 26},
            {rank: 4, country: "fra", gold: 16, silver: 26, bronze: 22},
            {rank: 5, country: "aus", gold: 18, silver: 19, bronze: 16},
        ];
        return data.slice(0, n);
    }
}

class MedalService{
    private provider: Paris2024Provider;

    constructor(){
        this.provider = new Paris2024Provider()
    }

    showTop(n: number){
        const rows = this.provider.top(n);

        console.log("\n=== Paris 2024 ===");
        console.table(rows);
    }
}

const medallero = new MedalService();
medallero.showTop(5);