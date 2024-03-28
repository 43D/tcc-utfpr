export type ApiType = {
    test: () => void;
}

export const Api = (): ApiType => {

    const test = () => {
        console.log("teste");
    }

    return {
        test
    }
}