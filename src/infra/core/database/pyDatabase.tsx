import { PyDatabaseType } from "../../../type/pywebview/index.d";

export const PyDatabase = (database: PyDatabaseType): PyDatabaseType => {
    const get_attr = (tag: string) => database.get_attr(tag);
    const update_attr = (tag: string, value: string) => database.update_attr(tag, value);

    return {
        get_attr,
        update_attr
    }
}