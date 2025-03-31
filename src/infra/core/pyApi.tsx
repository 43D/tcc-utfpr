import { pywebview, PywebviewApiType } from "../../type/pywebview/index.d";
import { PyDatabase } from "./database/pyDatabase";
import { PyUtils } from "./util/pyUtils";

export const PyApi = (pywv: pywebview): PywebviewApiType => {
    const utils = PyUtils(pywv.api.utils);
    const databaseController = PyDatabase(pywv.api.databaseController);

    return {
        utils,
        databaseController
    }

}